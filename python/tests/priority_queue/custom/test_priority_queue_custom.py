import pytest
from  data_structures.priority_queue.custom.priority_queue_custom import PriorityQueue


def test_push_pop_order_max_priority_queue():
    pq = PriorityQueue()  # uses MaxHeap internally; highest priority first
    pq.push("low", priority=1)
    pq.push("mid", priority=5)
    pq.push("high", priority=9)

    assert len(pq) == 3
    assert pq.pop() == "high"
    assert pq.pop() == "mid"
    assert pq.pop() == "low"
    assert pq.is_empty()


def test_stability_with_equal_priorities_fifo_among_equals():
    pq = PriorityQueue()
    pq.push("A", priority=10)  # arrives first
    pq.push("B", priority=10)  # arrives second
    pq.push("C", priority=10)  # arrives third

    # For equal priorities, FIFO should be preserved
    assert pq.pop() == "A"
    assert pq.pop() == "B"
    assert pq.pop() == "C"
    assert pq.is_empty()


def test_peek_does_not_remove():
    pq = PriorityQueue()
    pq.push("x", priority=2)
    pq.push("y", priority=7)
    pq.push("z", priority=5)

    # Highest priority is "y"
    assert pq.peek() == "y"
    # Should not remove
    assert len(pq) == 3

    # Still pops in the same order
    assert pq.pop() == "y"
    assert pq.pop() == "z"
    assert pq.pop() == "x"


def test_len_and_is_empty():
    pq = PriorityQueue()
    assert pq.is_empty()
    assert len(pq) == 0

    pq.push("a", priority=1)
    pq.push("b", priority=2)

    assert not pq.is_empty()
    assert len(pq) == 2

    _ = pq.pop()
    assert len(pq) == 1

    _ = pq.pop()
    assert pq.is_empty()
    assert len(pq) == 0


def test_pop_empty_raises():
    pq = PriorityQueue()
    with pytest.raises(IndexError):
        pq.pop()


def test_peek_empty_raises():
    pq = PriorityQueue()
    with pytest.raises(IndexError):
        pq.peek()


def test_mixed_equal_and_distinct_priorities():
    pq = PriorityQueue()
    pq.push("A1", priority=10)
    pq.push("B", priority=5)
    pq.push("A2", priority=10)
    pq.push("C", priority=7)
    pq.push("A3", priority=10)

    # All priority 10 first, preserving FIFO among them
    assert pq.pop() == "A1"
    assert pq.pop() == "A2"
    assert pq.pop() == "A3"
    # Then 7, then 5
    assert pq.pop() == "C"
    assert pq.pop() == "B"
    assert pq.is_empty()