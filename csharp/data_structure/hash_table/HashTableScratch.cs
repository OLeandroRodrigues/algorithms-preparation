using System;
using System.Collections.Generic;

namespace DataStructures.HashTable;

public class HashTableScratch<TKey, TValue>
{
    private class Node
    {
        public TKey Key;
        public TValue Value;
        public Node? Next;

        public Node(TKey key, TValue value, Node? next)
        {
            Key = key;
            Value = value;
            Next = next;
        }
    }

    private Node?[] _buckets;
    private int _capacity;
    private int _size;
    private readonly double _loadFactor;

    // -----------------------------
    //      Constructors
    // -----------------------------
    public HashTableScratch(int capacity, double loadFactor)
    {
        if (capacity <= 0)
            throw new ArgumentException("capacity must be > 0", nameof(capacity));

        if (loadFactor <= 0.0 || loadFactor >= 1.0)
            throw new ArgumentException("loadFactor must be in (0, 1)", nameof(loadFactor));

        _capacity = capacity;
        _loadFactor = loadFactor;
        _size = 0;
        _buckets = new Node?[capacity];
    }

    public HashTableScratch() : this(8, 0.75)
    {
    }

    // -----------------------------
    //      Internal helpers
    // -----------------------------
    private int Hash(TKey key)
    {
        // Handle with null in a safe way
        int h = key is null ? 0 : key.GetHashCode();
        return h & 0x7FFFFFFF; // force be negative
    }

    private int Index(TKey key)
    {
        return Hash(key) % _capacity;
    }

    private bool NeedsRehash()
    {
        return (double)_size / _capacity >= _loadFactor;
    }

    private void Rehash()
    {
        Node?[] oldBuckets = _buckets;
        _capacity *= 2;
        _buckets = new Node?[_capacity];
        _size = 0;

        foreach (Node? node in oldBuckets)
        {
            Node? current = node;
            while (current != null)
            {
                Put(current.Key, current.Value);
                current = current.Next;
            }
        }
    }

    // -----------------------------
    //       Public operations
    // -----------------------------
    public void Put(TKey key, TValue value)
    {
        if (NeedsRehash())
        {
            Rehash();
        }

        int idx = Index(key);
        Node? head = _buckets[idx];

        Node? current = head;
        var comparer = EqualityComparer<TKey>.Default;

        while (current != null)
        {
            if (comparer.Equals(current.Key, key))
            {
                current.Value = value; // update
                return;
            }
            current = current.Next;
        }

        Node newNode = new Node(key, value, head);
        _buckets[idx] = newNode;
        _size++;
    }

    public TValue Get(TKey key)
    {
        int idx = Index(key);
        Node? current = _buckets[idx];
        var comparer = EqualityComparer<TKey>.Default;

        while (current != null)
        {
            if (comparer.Equals(current.Key, key))
            {
                return current.Value;
            }
            current = current.Next;
        }

        throw new KeyNotFoundException($"Key not found: {key}");
    }

    public bool Remove(TKey key)
    {
        int idx = Index(key);
        Node? current = _buckets[idx];
        Node? prev = null;
        var comparer = EqualityComparer<TKey>.Default;

        while (current != null)
        {
            if (comparer.Equals(current.Key, key))
            {
                if (prev == null)
                {
                    _buckets[idx] = current.Next;
                }
                else
                {
                    prev.Next = current.Next;
                }

                _size--;
                return true;
            }

            prev = current;
            current = current.Next;
        }

        return false;
    }

    public bool Contains(TKey key)
    {
        int idx = Index(key);
        Node? current = _buckets[idx];
        var comparer = EqualityComparer<TKey>.Default;

        while (current != null)
        {
            if (comparer.Equals(current.Key, key))
            {
                return true;
            }
            current = current.Next;
        }

        return false;
    }

    public int Size()
    {
        return _size;
    }

    public double CurrentLoadFactor()
    {
        return (double)_size / _capacity;
    }

    public override string ToString()
    {
        var sb = new System.Text.StringBuilder();
        sb.Append("{ ");
        bool first = true;

        foreach (Node? bucket in _buckets)
        {
            Node? current = bucket;
            while (current != null)
            {
                if (!first)
                {
                    sb.Append(", ");
                }

                sb.Append(current.Key)
                    .Append(": ")
                    .Append(current.Value);

                first = false;
                current = current.Next;
            }
        }

        sb.Append(" }");
        return sb.ToString();
    }
}

