namespace DataStructures.LinkedList.CircularLinkedList;

public class CircularLinkedList<T>
{
    public class Node
    {
        public T Value;
        public Node Next;

        public Node(T value)
        {
            Value = value;
        }
    }

    public Node Tail;  // Tail.Next = head
    public int Size { get; private set; }

    public CircularLinkedList()
    {
        Tail = null;
        Size = 0;
    }

    public bool IsEmpty()
    {
        return Tail == null;
    }

    // Insert at beginning (head)
    public void AddFirst(T value)
    {
        var newNode = new Node(value);

        if (IsEmpty())
        {
            Tail = newNode;
            newNode.Next = newNode;   // circular
        }
        else
        {
            newNode.Next = Tail.Next; // current head
            Tail.Next = newNode;      // new head
        }

        Size++;
    }

    // Insert at end (tail)
    public void AddLast(T value)
    {
        AddFirst(value);
        Tail = Tail.Next; // move tail to new node
    }

    // Remove first (head)
    public T RemoveFirst()
    {
        if (IsEmpty())
            throw new InvalidOperationException("RemoveFirst from empty list");

        Node head = Tail.Next;
        T value = head.Value;

        if (Tail == head) // only one node
        {
            Tail = null;
        }
        else
        {
            Tail.Next = head.Next; // bypass old head
        }

        Size--;
        return value;
    }

    // Get first element
    public T GetFirst()
    {
        if (IsEmpty())
            throw new InvalidOperationException("GetFirst from empty list");

        return Tail.Next.Value; // head
    }

    // Get last element
    public T GetLast()
    {
        if (IsEmpty())
            throw new InvalidOperationException("GetLast from empty list");

        return Tail.Value;
    }

    // Find value in the cycle
    public Node Find(T value)
    {
        if (IsEmpty())
            return null;

        Node current = Tail.Next; // head

        while (true)
        {
            if ((current.Value == null && value == null) ||
                (current.Value != null && current.Value.Equals(value)))
            {
                return current;
            }

            current = current.Next;

            if (current == Tail.Next) // full cycle
                break;
        }

        return null;
    }

    public override string ToString()
    {
        if (IsEmpty())
            return "CircularLinkedList([])";

        var sb = new System.Text.StringBuilder("CircularLinkedList([");
        Node current = Tail.Next; // head

        while (true)
        {
            sb.Append(current.Value);
            current = current.Next;

            if (current == Tail.Next)
                break;

            sb.Append(", ");
        }

        sb.Append("])");
        return sb.ToString();
    }
}

