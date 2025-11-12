import pytest

from data_structures.queue.queue import Queue

def test_enqueue_dequeue_order():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.is_empty()

def test_peek_does_not_remove():
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    assert q.peek() == "a"
    assert q.size() == 2
    assert q.dequeue() == "a"
    assert q.peek() == "b"
    assert q.size() == 1

def test_is_empty_and_size():
    q = Queue()
    assert q.is_empty()
    assert q.size() == 0
    q.enqueue(42)
    assert not q.is_empty()
    assert q.size() == 1

def test_dequeue_empty_raises():
    q = Queue()
    with pytest.raises(IndexError, match="dequeue from empty queue"):
        q.dequeue()

def test_peek_empty_raises():
    q = Queue()
    with pytest.raises(IndexError, match="peek from empty queue"):
        q.peek()
