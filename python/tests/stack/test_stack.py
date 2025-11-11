import pytest
from data_structures.stack.stack import Stack

class TestStack:
    
    def test_push_and_peek(self):
        s = Stack()
        assert s.is_empty()

        s.push(10)
        s.push(20)
        s.push(30)

        # top should be the last pushed element
        assert s.peek() == 30
        assert not s.is_empty()
        assert s.size() == 3
        print("test_push_and_peek passed successfully!")

    def test_pop_follows_lifo_order(self):
        s = Stack()
        for i in [1, 2, 3]:
            s.push(i)

        assert s.pop() == 3
        assert s.pop() == 2
        assert s.pop() == 1
        assert s.is_empty()
        print("test_pop_follows_lifo_order passed successfully!")

    def test_peek_does_not_remove_element(self):
        s = Stack()
        s.push("A")
        top = s.peek()
        assert top == "A"
        assert not s.is_empty()
        assert s.size() == 1
        print("test_peek_does_not_remove_element passed successfully!")

    def test_pop_from_empty_stack_raises(self):
        s = Stack()
        with pytest.raises(IndexError, match="pop from empty stack"):
            s.pop()
        print("test_pop_from_empty_stack_raises passed successfully!")

    def test_peek_from_empty_stack_raises(self):
        s = Stack()
        with pytest.raises(IndexError, match="peek from empty stack"):
            s.peek()
        print("test_peek_from_empty_stack_raises passed successfully!")

    def test_repr_outputs_readable_string(self):
        s = Stack()
        s.push(1)
        s.push(2)
        assert "Stack" in repr(s)
        assert "[1, 2]" in repr(s)
        print("test_repr_outputs_readable_string passed successfully!")
