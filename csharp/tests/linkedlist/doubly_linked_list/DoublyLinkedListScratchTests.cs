using System;
using System.Collections.Generic;
using DataStructures.LinkedList.DoublyLinkedList;
using Xunit;

namespace DataStructures.Tests.LinkedList.DoublyLinkedList
{
    public class DoublyLinkedListScratchTests
    {
        private DoublyLinkedListScratch<int> CreateList()
        {
            return new DoublyLinkedListScratch<int>();
        }

        private List<int> ToList(DoublyLinkedListScratch<int> list)
        {
            var result = new List<int>();
            var current = list.GetHead();
            while (current != null)
            {
                result.Add(current.GetValue());
                current = current.GetNext();
            }
            return result;
        }

        [Fact]
        public void InitialState_ShouldBeEmpty()
        {
            var list = CreateList();

            Assert.True(list.IsEmpty());
            Assert.Equal(0, list.Size());
            Assert.Null(list.GetHead());
            Assert.Null(list.GetTail());
            Assert.Equal("DoublyLinkedListScratch[]", list.ToString());
        }

        [Fact]
        public void PushFront_OnEmptyList_SetsHeadAndTail()
        {
            var list = CreateList();

            var n = list.PushFront(10);

            Assert.False(list.IsEmpty());
            Assert.Equal(1, list.Size());
            Assert.Same(n, list.GetHead());
            Assert.Same(n, list.GetTail());
            Assert.Null(n.GetPrev());
            Assert.Null(n.GetNext());
            Assert.Equal(new List<int> { 10 }, ToList(list));
        }

        [Fact]
        public void PushFront_OnNonEmptyList_UpdatesHead()
        {
            var list = CreateList();

            var n1 = list.PushFront(10);
            var n2 = list.PushFront(20);

            Assert.Equal(2, list.Size());
            Assert.Same(n2, list.GetHead());
            Assert.Same(n1, list.GetTail());
            Assert.Null(n2.GetPrev());
            Assert.Same(n1, n2.GetNext());
            Assert.Same(n2, n1.GetPrev());
            Assert.Null(n1.GetNext());

            Assert.Equal(new List<int> { 20, 10 }, ToList(list));
        }

        [Fact]
        public void PushBack_OnEmptyList_SetsHeadAndTail()
        {
            var list = CreateList();

            var n = list.PushBack(10);

            Assert.False(list.IsEmpty());
            Assert.Equal(1, list.Size());
            Assert.Same(n, list.GetHead());
            Assert.Same(n, list.GetTail());
            Assert.Null(n.GetPrev());
            Assert.Null(n.GetNext());
            Assert.Equal(new List<int> { 10 }, ToList(list));
        }

        [Fact]
        public void PushBack_OnNonEmptyList_UpdatesTail()
        {
            var list = CreateList();

            var n1 = list.PushBack(10);
            var n2 = list.PushBack(20);

            Assert.Equal(2, list.Size());
            Assert.Same(n1, list.GetHead());
            Assert.Same(n2, list.GetTail());
            Assert.Null(n1.GetPrev());
            Assert.Same(n2, n1.GetNext());
            Assert.Same(n1, n2.GetPrev());
            Assert.Null(n2.GetNext());

            Assert.Equal(new List<int> { 10, 20 }, ToList(list));
        }

        [Fact]
        public void InsertAfter_MiddleNode_InsertsBetweenNodes()
        {
            var list = CreateList();

            var n1 = list.PushBack(10);
            var n2 = list.PushBack(20);
            var n3 = list.PushBack(30);

            var nNew = list.InsertAfter(n1, 15);

            Assert.Equal(4, list.Size());
            Assert.Same(nNew, n1.GetNext());
            Assert.Same(n1, nNew.GetPrev());
            Assert.Same(n2, nNew.GetNext());
            Assert.Same(nNew, n2.GetPrev());

            Assert.Equal(new List<int> { 10, 15, 20, 30 }, ToList(list));
        }

        [Fact]
        public void InsertAfter_Tail_DelegatesToPushBack()
        {
            var list = CreateList();

            var n1 = list.PushBack(10);
            var n2 = list.PushBack(20);

            var nNew = list.InsertAfter(n2, 30);

            Assert.Equal(3, list.Size());
            Assert.Same(nNew, list.GetTail());
            Assert.Equal(new List<int> { 10, 20, 30 }, ToList(list));
        }

        [Fact]
        public void InsertAfter_NullNode_Throws()
        {
            var list = CreateList();

            Assert.Throws<ArgumentNullException>(
                () => list.InsertAfter(null, 10)
            );
        }

        [Fact]
        public void InsertBefore_MiddleNode_InsertsBetweenNodes()
        {
            var list = CreateList();

            var n1 = list.PushBack(10);
            var n2 = list.PushBack(20);
            var n3 = list.PushBack(30);

            var nNew = list.InsertBefore(n2, 15);

            Assert.Equal(4, list.Size());
            Assert.Same(nNew, n1.GetNext());
            Assert.Same(n1, nNew.GetPrev());
            Assert.Same(n2, nNew.GetNext());
            Assert.Same(nNew, n2.GetPrev());

            Assert.Equal(new List<int> { 10, 15, 20, 30 }, ToList(list));
        }

        [Fact]
        public void InsertBefore_Head_DelegatesToPushFront()
        {
            var list = CreateList();

            var n1 = list.PushBack(10);
            var n2 = list.PushBack(20);

            var nNew = list.InsertBefore(n1, 5);

            Assert.Equal(3, list.Size());
            Assert.Same(nNew, list.GetHead());
            Assert.Equal(new List<int> { 5, 10, 20 }, ToList(list));
        }

        [Fact]
        public void InsertBefore_NullNode_Throws()
        {
            var list = CreateList();

            Assert.Throws<ArgumentNullException>(
                () => list.InsertBefore(null, 10)
            );
        }

        [Fact]
        public void PopFront_SingleElement_ClearsList()
        {
            var list = CreateList();
            list.PushBack(10);

            var value = list.PopFront();

            Assert.Equal(10, value);
            Assert.True(list.IsEmpty());
            Assert.Null(list.GetHead());
            Assert.Null(list.GetTail());
        }

        [Fact]
        public void PopFront_MultipleElements_MovesHead()
        {
            var list = CreateList();
            list.PushBack(10);
            list.PushBack(20);

            var value = list.PopFront();

            Assert.Equal(10, value);
            Assert.Equal(1, list.Size());
            Assert.Equal(new List<int> { 20 }, ToList(list));
            Assert.Null(list.GetHead().GetPrev());
        }

        [Fact]
        public void PopFront_OnEmptyList_Throws()
        {
            var list = CreateList();

            Assert.Throws<InvalidOperationException>(
                () => list.PopFront()
            );
        }

        [Fact]
        public void PopBack_SingleElement_ClearsList()
        {
            var list = CreateList();
            list.PushBack(10);

            var value = list.PopBack();

            Assert.Equal(10, value);
            Assert.True(list.IsEmpty());
            Assert.Null(list.GetHead());
            Assert.Null(list.GetTail());
        }

        [Fact]
        public void PopBack_MultipleElements_MovesTail()
        {
            var list = CreateList();
            list.PushBack(10);
            list.PushBack(20);

            var value = list.PopBack();

            Assert.Equal(20, value);
            Assert.Equal(1, list.Size());
            Assert.Equal(new List<int> { 10 }, ToList(list));
            Assert.Null(list.GetTail().GetNext());
        }

        [Fact]
        public void PopBack_OnEmptyList_Throws()
        {
            var list = CreateList();

            Assert.Throws<InvalidOperationException>(
                () => list.PopBack()
            );
        }

        [Fact]
        public void Remove_SingleNode_ClearsList()
        {
            var list = CreateList();
            var n = list.PushBack(10);

            var removed = list.Remove(n);

            Assert.Equal(10, removed);
            Assert.True(list.IsEmpty());
            Assert.Null(list.GetHead());
            Assert.Null(list.GetTail());
        }

        [Fact]
        public void Remove_HeadInMultiElementList_UpdatesHead()
        {
            var list = CreateList();
            var n1 = list.PushBack(10);
            list.PushBack(20);
            list.PushBack(30);

            var removed = list.Remove(n1);

            Assert.Equal(10, removed);
            Assert.Equal(2, list.Size());
            Assert.Equal(20, list.GetHead().GetValue());
            Assert.Null(list.GetHead().GetPrev());
            Assert.Equal(new List<int> { 20, 30 }, ToList(list));
        }

        [Fact]
        public void Remove_TailInMultiElementList_UpdatesTail()
        {
            var list = CreateList();
            list.PushBack(10);
            list.PushBack(20);
            var n3 = list.PushBack(30);

            var removed = list.Remove(n3);

            Assert.Equal(30, removed);
            Assert.Equal(2, list.Size());
            Assert.Equal(20, list.GetTail().GetValue());
            Assert.Null(list.GetTail().GetNext());
            Assert.Equal(new List<int> { 10, 20 }, ToList(list));
        }

        [Fact]
        public void Remove_MiddleNode_LinksNeighbors()
        {
            var list = CreateList();
            var n1 = list.PushBack(10);
            var n2 = list.PushBack(20);
            var n3 = list.PushBack(30);

            var removed = list.Remove(n2);

            Assert.Equal(20, removed);
            Assert.Equal(2, list.Size());
            Assert.Same(n3, n1.GetNext());
            Assert.Same(n1, n3.GetPrev());
            Assert.Equal(new List<int> { 10, 30 }, ToList(list));
        }

        [Fact]
        public void Remove_NullNode_Throws()
        {
            var list = CreateList();

            Assert.Throws<ArgumentNullException>(
                () => list.Remove(null)
            );
        }

        [Fact]
        public void Remove_FromEmptyList_Throws()
        {
            var list = CreateList();
            var fakeNode = new DoublyLinkedListScratch<int>.Node(10);

            Assert.Throws<InvalidOperationException>(
                () => list.Remove(fakeNode)
            );
        }

        [Fact]
        public void Find_ExistingValue_ReturnsNode()
        {
            var list = CreateList();
            list.PushBack(10);
            list.PushBack(20);
            list.PushBack(30);

            var found = list.Find(20);

            Assert.NotNull(found);
            Assert.Equal(20, found.GetValue());
        }

        [Fact]
        public void Find_MissingValue_ReturnsNull()
        {
            var list = CreateList();
            list.PushBack(10);
            list.PushBack(20);

            var found = list.Find(99);

            Assert.Null(found);
        }


        [Fact]
        public void ToString_ContainsValuesInOrder()
        {
            var list = CreateList();
            list.PushBack(1);
            list.PushBack(2);
            list.PushBack(3);

            var s = list.ToString();

            Assert.StartsWith("DoublyLinkedListScratch[", s);
            Assert.Contains("1", s);
            Assert.Contains("2", s);
            Assert.Contains("3", s);
        }
    }
}
