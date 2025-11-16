using System;
using System.Collections.Generic;
using System.Text;

namespace DataStructures.LinkedList.DoublyLinkedList
{
    public class DoublyLinkedListScratch<T>
    {
        public class Node
        {
            internal T Value;
            internal Node Prev;
            internal Node Next;

            public Node(T value)
            {
                Value = value;
            }

            public T GetValue() => Value;
            public Node GetPrev() => Prev;
            public Node GetNext() => Next;

            public override string ToString()
            {
                return $"Node({Value})";
            }
        }

        private Node _head;
        private Node _tail;
        private int _sizeValue;

        public DoublyLinkedListScratch()
        {
            _head = null;
            _tail = null;
            _sizeValue = 0;
        }

        public bool IsEmpty()
        {
            return _sizeValue == 0;
        }

        public int Size()
        {
            return _sizeValue;
        }

        private Node MakeNode(T value)
        {
            return new Node(value);
        }

        public Node GetHead()
        {
            return _head;
        }

        public Node GetTail()
        {
            return _tail;
        }

        public Node PushFront(T value)
        {
            Node n = MakeNode(value);

            n.Next = _head;

            if (_head != null)
            {
                _head.Prev = n;
            }
            else
            {
                _tail = n;
            }

            _head = n;
            _sizeValue++;
            return n;
        }

        public Node PushBack(T value)
        {
            Node n = MakeNode(value);

            if (_tail == null)
            {
                _head = _tail = n;
            }
            else
            {
                n.Prev = _tail;
                _tail.Next = n;
                _tail = n;
            }

            _sizeValue++;
            return n;
        }

        public Node InsertAfter(Node node, T value)
        {
            if (node == null)
            {
                throw new ArgumentNullException(nameof(node), "InsertAfter: node cannot be null");
            }

            if (node == _tail)
            {
                return PushBack(value);
            }

            Node n = MakeNode(value);
            Node successor = node.Next;

            n.Prev = node;
            n.Next = successor;

            node.Next = n;
            if (successor != null)
            {
                successor.Prev = n;
            }

            _sizeValue++;
            return n;
        }

        public Node InsertBefore(Node node, T value)
        {
            if (node == null)
            {
                throw new ArgumentNullException(nameof(node), "InsertBefore: node cannot be null");
            }

            if (node == _head)
            {
                return PushFront(value);
            }

            Node n = MakeNode(value);
            Node predecessor = node.Prev;

            n.Next = node;
            n.Prev = predecessor;

            if (predecessor != null)
            {
                predecessor.Next = n;
            }
            node.Prev = n;

            _sizeValue++;
            return n;
        }

        public T PopFront()
        {
            if (IsEmpty())
            {
                throw new InvalidOperationException("PopFront from empty list");
            }

            Node node = _head;
            T value = node.Value;

            if (_head == _tail)
            {
                _head = _tail = null;
            }
            else
            {
                _head = _head.Next;
                _head.Prev = null;
            }

            _sizeValue--;
            return value;
        }

        public T PopBack()
        {
            if (IsEmpty())
            {
                throw new InvalidOperationException("PopBack from empty list");
            }

            Node node = _tail;
            T value = node.Value;

            if (_head == _tail)
            {
                _head = _tail = null;
            }
            else
            {
                _tail = _tail.Prev;
                _tail.Next = null;
            }

            _sizeValue--;
            return value;
        }

        public T Remove(Node node)
        {
            if (node == null)
            {
                throw new ArgumentNullException(nameof(node), "Remove: node cannot be null");
            }

            if (IsEmpty())
            {
                throw new InvalidOperationException("Remove from empty list");
            }

            if (node == _head && node == _tail)
            {
                _head = _tail = null;
            }

            else if (node == _head)
            {
                _head = node.Next;
                _head.Prev = null;
            }
     
            else if (node == _tail)
            {
                _tail = node.Prev;
                _tail.Next = null;
            }
     
            else
            {
                Node prevNode = node.Prev;
                Node nextNode = node.Next;
                prevNode.Next = nextNode;
                nextNode.Prev = prevNode;
            }

            node.Prev = null;
            node.Next = null;

            _sizeValue--;
            return node.Value;
        }

        public Node Find(T value)
        {
            var comparer = EqualityComparer<T>.Default;
            Node current = _head;

            while (current != null)
            {
                if (comparer.Equals(current.Value, value))
                {
                    return current;
                }
                current = current.Next;
            }
            return null;
        }

        public override string ToString()
        {
            var sb = new StringBuilder("DoublyLinkedListScratch[");
            Node current = _head;

            while (current != null)
            {
                sb.Append(current.Value);
                if (current.Next != null)
                {
                    sb.Append(", ");
                }
                current = current.Next;
            }

            sb.Append("]");
            return sb.ToString();
        }
    }
}
