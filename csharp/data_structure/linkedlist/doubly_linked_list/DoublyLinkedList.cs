using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;

namespace DataStructures.LinkedList;

/// <summary>
/// A simple, production-ready implementation of a doubly linked list.
///
/// Supports O(1) insertion and removal at both ends, forward iteration,
/// and a reversed enumerable.
/// Not thread-safe.
/// </summary>
/// <typeparam name="T">Element type.</typeparam>
public class DoublyLinkedList<T> : IEnumerable<T>
{
    /// <summary>
    /// Internal node representation. Not exposed outside this class.
    /// </summary>
    private sealed class Node
    {
        public T Item;
        public Node? Prev;
        public Node? Next;

        public Node(Node? prev, T item, Node? next)
        {
            Prev = prev;
            Item = item;
            Next = next;
        }
    }

    private Node? _head;
    private Node? _tail;
    private int _count;

    /// <summary>
    /// Creates an empty list.
    /// </summary>
    public DoublyLinkedList()
    {
    }

    /// <summary>
    /// Creates a list populated with all elements from the given sequence,
    /// in iteration order.
    /// </summary>
    public DoublyLinkedList(IEnumerable<T> source)
    {
        if (source is null) throw new ArgumentNullException(nameof(source));
        foreach (var item in source)
        {
            AddLast(item);
        }
    }

    /// <summary>
    /// Gets the number of elements in the list.
    /// </summary>
    public int Count => _count;

    /// <summary>
    /// Returns true if the list contains no elements.
    /// </summary>
    public bool IsEmpty => _count == 0;

    /// <summary>
    /// Removes all elements from the list.
    /// </summary>
    public void Clear()
    {
        var current = _head;
        while (current is not null)
        {
            var next = current.Next;
            current.Prev = null;
            current.Next = null;
            current.Item = default!;
            current = next;
        }

        _head = _tail = null;
        _count = 0;
    }

    // --------------------------------------------------------------------
    // Core operations: add / remove / peek at both ends
    // --------------------------------------------------------------------

    /// <summary>
    /// Inserts an element at the beginning of the list.
    /// </summary>
    public void AddFirst(T value)
    {
        var newNode = new Node(prev: null, item: value, next: _head);

        if (_head is null)
        {
            // list was empty
            _head = _tail = newNode;
        }
        else
        {
            _head.Prev = newNode;
            _head = newNode;
        }

        _count++;
    }

    /// <summary>
    /// Inserts an element at the end of the list.
    /// </summary>
    public void AddLast(T value)
    {
        var newNode = new Node(prev: _tail, item: value, next: null);

        if (_tail is null)
        {
            // list was empty
            _head = _tail = newNode;
        }
        else
        {
            _tail.Next = newNode;
            _tail = newNode;
        }

        _count++;
    }

    /// <summary>
    /// Returns, but does not remove, the first element of the list.
    /// </summary>
    /// <exception cref="InvalidOperationException">If the list is empty.</exception>
    public T PeekFirst()
    {
        if (_head is null)
            throw new InvalidOperationException("PeekFirst from empty list");
        return _head.Item;
    }

    /// <summary>
    /// Returns, but does not remove, the last element of the list.
    /// </summary>
    /// <exception cref="InvalidOperationException">If the list is empty.</exception>
    public T PeekLast()
    {
        if (_tail is null)
            throw new InvalidOperationException("PeekLast from empty list");
        return _tail.Item;
    }

    /// <summary>
    /// Removes and returns the first element of the list.
    /// </summary>
    /// <exception cref="InvalidOperationException">If the list is empty.</exception>
    public T RemoveFirst()
    {
        if (_head is null)
        {
            throw new InvalidOperationException("RemoveFirst from empty list");
        }

        var node = _head;
        var value = node.Item;

        if (_head == _tail)
        {
            // single element
            _head = _tail = null;
        }
        else
        {
            _head = _head.Next;
            if (_head is not null)
            {
                _head.Prev = null;
            }
        }

        node.Next = null;
        node.Item = default!;
        _count--;
        return value;
    }

    /// <summary>
    /// Removes and returns the last element of the list.
    /// </summary>
    /// <exception cref="InvalidOperationException">If the list is empty.</exception>
    public T RemoveLast()
    {
        if (_tail is null)
        {
            throw new InvalidOperationException("RemoveLast from empty list");
        }

        var node = _tail;
        var value = node.Item;

        if (_head == _tail)
        {
            _head = _tail = null;
        }
        else
        {
            _tail = _tail.Prev;
            if (_tail is not null)
            {
                _tail.Next = null;
            }
        }

        node.Prev = null;
        node.Item = default!;
        _count--;
        return value;
    }

    // --------------------------------------------------------------------
    // Search / removal by value
    // --------------------------------------------------------------------

    /// <summary>
    /// Returns true if the list contains at least one element equal to the given value.
    /// Uses EqualityComparer&lt;T&gt;.Default for comparison.
    /// </summary>
    public bool Contains(T value)
    {
        return FindNode(value) is not null;
    }

    /// <summary>
    /// Removes the first occurrence of the given value from the list, if present.
    /// Uses EqualityComparer&lt;T&gt;.Default for comparison.
    /// </summary>
    /// <returns>true if an element was removed; false otherwise.</returns>
    public bool RemoveFirstOccurrence(T value)
    {
        var node = FindNode(value);
        if (node is null)
        {
            return false;
        }

        Unlink(node);
        return true;
    }

    private Node? FindNode(T value)
    {
        var comparer = EqualityComparer<T>.Default;
        var current = _head;

        while (current is not null)
        {
            if (comparer.Equals(current.Item, value))
            {
                return current;
            }
            current = current.Next;
        }

        return null;
    }

    /// <summary>
    /// Unlinks the given node from the list, adjusting head/tail and count.
    /// Assumes the node belongs to this list.
    /// </summary>
    private void Unlink(Node node)
    {
        var prev = node.Prev;
        var next = node.Next;

        if (prev is null)
        {
            // node is head
            _head = next;
        }
        else
        {
            prev.Next = next;
        }

        if (next is null)
        {
            // node is tail
            _tail = prev;
        }
        else
        {
            next.Prev = prev;
        }

        node.Prev = null;
        node.Next = null;
        node.Item = default!;
        _count--;
    }

    // --------------------------------------------------------------------
    // Iteration
    // --------------------------------------------------------------------

    /// <summary>
    /// Returns an enumerator that iterates through the list from first to last.
    /// </summary>
    public IEnumerator<T> GetEnumerator()
    {
        return new ForwardEnumerator(this);
    }

    IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();

    private sealed class ForwardEnumerator : IEnumerator<T>
    {
        private readonly DoublyLinkedList<T> _list;
        private Node? _current;
        private Node? _lastReturned;

        public ForwardEnumerator(DoublyLinkedList<T> list)
        {
            _list = list;
            _current = list._head;
        }

        public T Current
        {
            get
            {
                if (_lastReturned is null)
                    throw new InvalidOperationException("Enumeration has not started. Call MoveNext.");
                return _lastReturned.Item;
            }
        }

        object IEnumerator.Current => Current!;

        public bool MoveNext()
        {
            if (_current is null)
            {
                _lastReturned = null;
                return false;
            }

            _lastReturned = _current;
            _current = _current.Next;
            return true;
        }

        public void Reset()
        {
            _current = _list._head;
            _lastReturned = null;
        }

        public void Dispose()
        {
            // nothing to dispose
        }
    }

    /// <summary>
    /// Returns an enumerable that iterates the elements in reverse order
    /// (from last to first).
    /// </summary>
    public IEnumerable<T> AsReversed()
    {
        return AsReversedIterator();

        IEnumerable<T> AsReversedIterator()
        {
            var current = _tail;
            while (current is not null)
            {
                yield return current.Item;
                current = current.Prev;
            }
        }
    }

    // --------------------------------------------------------------------
    // ToString / debug
    // --------------------------------------------------------------------

    public override string ToString()
    {
        var sb = new StringBuilder();
        sb.Append("DoublyLinkedList[");

        var current = _head;
        while (current is not null)
        {
            sb.Append(current.Item);
            if (current.Next is not null)
            {
                sb.Append(", ");
            }
            current = current.Next;
        }

        sb.Append(']');
        return sb.ToString();
    }
}
