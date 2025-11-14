using System;
using Xunit;
using DataStructures.LinkedList;

namespace DataStructures.LinkedList.Tests
{
    public class SinglyLinkedListScratchTests
    {
        [Fact]
        public void PushFront_ShouldInsertAtBeginning()
        {
            var list = new SinglyLinkedListScratch();

            list.PushFront(3); // [3]
            list.PushFront(2); // [2, 3]
            list.PushFront(1); // [1, 2, 3]

            Assert.Equal(3, list.Size());
            Assert.NotNull(list.GetHead());
            Assert.Equal(1, list.GetHead().Value);
            Assert.Equal(2, list.GetHead().Next.Value);
            Assert.NotNull(list.GetTail());
            Assert.Equal(3, list.GetTail().Value);
        }

        [Fact]
        public void PushBack_ShouldInsertAtEnd()
        {
            var list = new SinglyLinkedListScratch();

            list.PushBack(1); // [1]
            list.PushBack(2); // [1, 2]
            list.PushBack(3); // [1, 2, 3]

            Assert.Equal(3, list.Size());
            Assert.Equal(1, list.GetHead().Value);
            Assert.Equal(3, list.GetTail().Value);
            Assert.Equal(2, list.GetHead().Next.Value);
        }

        [Fact]
        public void InsertAfter_MiddleNode_ShouldInsertCorrectly()
        {
            var list = new SinglyLinkedListScratch();

            var n1 = list.PushBack(1);
            var n2 = list.PushBack(2);
            list.PushBack(4); // [1, 2, 4]

            list.InsertAfter(n2, 3); // [1, 2, 3, 4]

            Assert.Equal(4, list.Size());
            Assert.Equal(2, n2.Value);
            Assert.NotNull(n2.Next);
            Assert.Equal(3, n2.Next.Value);
            Assert.Equal(4, n2.Next.Next.Value);
        }

        [Fact]
        public void InsertAfter_TailNode_ShouldUpdateTail()
        {
            var list = new SinglyLinkedListScratch();

            list.PushBack(1);
            var last = list.PushBack(2); // tail = 2

            list.InsertAfter(last, 3); // [1, 2, 3]

            Assert.Equal(3, list.Size());
            Assert.Equal(3, list.GetTail().Value);
            Assert.Equal(2, last.Value);
            Assert.Equal(3, last.Next.Value);
        }

        [Fact]
        public void PopFront_ShouldRemoveFirstElement()
        {
            var list = new SinglyLinkedListScratch();

            list.PushBack(10);
            list.PushBack(20);
            list.PushBack(30); // [10, 20, 30]

            var value = list.PopFront(); // remove 10 -> [20, 30]

            Assert.Equal(10, value);
            Assert.Equal(2, list.Size());
            Assert.Equal(20, list.GetHead().Value);
            Assert.Equal(30, list.GetTail().Value);
        }

        [Fact]
        public void PopFront_UntilEmpty_ShouldLeaveListEmpty()
        {
            var list = new SinglyLinkedListScratch();

            list.PushBack(1);
            list.PushBack(2);

            Assert.Equal(1, list.PopFront());
            Assert.Equal(2, list.PopFront());

            Assert.True(list.IsEmpty());
            Assert.Null(list.GetHead());
            Assert.Null(list.GetTail());
        }

        [Fact]
        public void PopFront_OnEmptyList_ShouldThrow()
        {
            var list = new SinglyLinkedListScratch();

            Assert.Throws<InvalidOperationException>(() => list.PopFront());
        }

        [Fact]
        public void RemoveAfter_MiddleNode_ShouldRemoveCorrectNode()
        {
            var list = new SinglyLinkedListScratch();

            var n1 = list.PushBack(1);
            var n2 = list.PushBack(2);
            list.PushBack(3); // [1, 2, 3]

            var removed = list.RemoveAfter(n1); // remove 2 -> [1, 3]

            Assert.Equal(2, removed);
            Assert.Equal(2, list.Size());
            Assert.Equal(1, list.GetHead().Value);
            Assert.Equal(3, list.GetHead().Next.Value);
            Assert.Equal(3, list.GetTail().Value);
        }

        [Fact]
        public void RemoveAfter_WhenNoNextNode_ShouldThrow()
        {
            var list = new SinglyLinkedListScratch();

            var n1 = list.PushBack(1); // [1]

            Assert.Throws<ArgumentException>(() => list.RemoveAfter(n1));
        }

        [Fact]
        public void InsertAfter_NullNode_ShouldThrow()
        {
            var list = new SinglyLinkedListScratch();

            Assert.Throws<ArgumentException>(() => list.InsertAfter(null, 10));
        }

        [Fact]
        public void Find_ShouldReturnNode_WhenValueExists()
        {
            var list = new SinglyLinkedListScratch();

            list.PushBack("A");
            list.PushBack("B");
            list.PushBack("C");

            var found = list.Find("B");

            Assert.NotNull(found);
            Assert.Equal("B", found.Value);
        }

        [Fact]
        public void Find_ShouldReturnNull_WhenValueDoesNotExist()
        {
            var list = new SinglyLinkedListScratch();

            list.PushBack("A");
            list.PushBack("B");
            list.PushBack("C");

            var notFound = list.Find("X");

            Assert.Null(notFound);
        }

        [Fact]
        public void IsEmpty_And_Size_ShouldReflectState()
        {
            var list = new SinglyLinkedListScratch();

            Assert.True(list.IsEmpty());
            Assert.Equal(0, list.Size());

            list.PushBack(1);
            list.PushBack(2);

            Assert.False(list.IsEmpty());
            Assert.Equal(2, list.Size());
        }
    }
}
