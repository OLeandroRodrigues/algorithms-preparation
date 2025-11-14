using System;
namespace DataStructures.LinkedList;

public class SinglyLinkedListScratch
{
    public class Node
    {
        public object Value;
        public Node Next;

        public Node(object value)
        {
            Value = value;
            Next = null;
        }
    }

    private Node head;
    private Node tail;
    private int sizeValue;

    public SinglyLinkedListScratch()
    {
        head = null;
        tail = null;
        sizeValue = 0;
    }

    private Node MakeNode(object value)
    {
        return new Node(value);
    }

    public Node PushFront(object value)
    {
        Node n = MakeNode(value);
        n.Next = head;
        head = n;

        if (tail == null)
        {
            tail = n;
        }

        sizeValue++;
        return n;
    }

    public Node PushBack(object value)
    {
        Node n = MakeNode(value);

        if (tail == null)
        {
            head = tail = n;
        }
        else
        {
            tail.Next = n;
            tail = n;
        }

        sizeValue++;
        return n;
    }

    public Node InsertAfter(Node node, object value)
    {
        if (node == null)
        {
            throw new ArgumentException("insert_after: node cannot be null");
        }

        Node n = MakeNode(value);
        n.Next = node.Next;
        node.Next = n;

        if (tail == node)
        {
            tail = n;
        }

        sizeValue++;
        return n;
    }

    public object PopFront()
    {
        if (head == null)
            throw new InvalidOperationException("pop_front from empty list");

        object value = head.Value;
        head = head.Next;
        sizeValue--;

        if (head == null)
            tail = null;

        return value;
    }

    public object RemoveAfter(Node node)
    {
        if (node == null || node.Next == null)
            throw new ArgumentException("remove_after: nothing to remove");


        Node toRemove = node.Next;
        node.Next = toRemove.Next;

        if (tail == toRemove)
        {
            tail = node;
        }

        sizeValue--;
        return toRemove.Value;
    }

    public Node Find(object value)
    {
        Node current = head;

        while (current != null)
        {
            if ((current.Value == null && value == null) ||
                (current.Value != null && current.Value.Equals(value)))
            {
                return current;
            }

            current = current.Next;
        }

        return null;
    }

    public bool IsEmpty()
    {
        return sizeValue == 0;
    }

    public int Size()
    {
        return sizeValue;
    }

    public Node GetHead()
    {
        return head;
    }

    public Node GetTail()
    {
        return tail;
    }
}

