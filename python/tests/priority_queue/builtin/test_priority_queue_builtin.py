import pytest
from data_structures.priority_queue.builtin.priority_queue_builtin import PriorityQueue

def test_max_priority_and_stability():
    pq = PriorityQueue(is_min=False)
    pq.push("A", 10)
    pq.push("B", 10)
    pq.push("C", 5)

    assert pq.peek() == "A"
    assert pq.pop() == "A"
    assert pq.pop() == "B"
    assert pq.pop() == "C"
    assert pq.is_empty()

def test_min_priority_basic():
    pq = PriorityQueue(is_min=True)
    pq.push("X", 3)
    pq.push("Y", 1)
    pq.push("Z", 2)

    assert pq.pop() == "Y"
    assert pq.pop() == "Z"
    assert pq.pop() == "X"

def test_empty_errors():
    pq = PriorityQueue()
    with pytest.raises(IndexError):
        pq.pop()
    with pytest.raises(IndexError):
        pq.peek()