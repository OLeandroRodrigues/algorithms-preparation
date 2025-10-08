from data_structures.heap.max_heap import MaxHeap
from typing import Any
import itertools

class PriorityQueue:
    """Priority Queue implementation using the existing MaxHeap.

    Each element is stored as a tuple (priority, -order, value) to ensure:
        - Higher 'priority' values are served first (max-priority behavior)
        - FIFO stability between elements with the same priority
          (via the negative order value)

    Time Complexity:
        - push(): O(log n)
        - pop():  O(log n)
        - peek(): O(1)
        - is_empty(), __len__(): O(1)
    """

    def __init__(self) -> None:
        """Initialize an empty priority queue."""
        self._heap = MaxHeap()
        self._order = itertools.count()  # Monotonic counter for stability

    def push(self, value: Any, priority: int) -> None:
        """Insert a new element with a given priority.

        Args:
            value (Any): The element to be inserted.
            priority (int): The priority of the element.
        """
        order = next(self._order)
        # The tuple is ordered so that the MaxHeap compares (priority, -order)
        # ensuring highest priority first, and FIFO order for equal priorities.
        self._heap.insert((priority, -order, value))

    def pop(self) -> Any:
        """Remove and return the element with the highest priority.

        Returns:
            Any: The value of the element with the highest priority.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("pop from an empty priority queue")

        priority, neg_order, value = self._heap.pop()
        return value

    def peek(self) -> Any:
        """Return the element with the highest priority without removing it.

        Returns:
            Any: The value of the element with the highest priority.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("peek from an empty priority queue")

        priority, neg_order, value = self._heap._data[0]
        return value

    def is_empty(self) -> bool:
        """Check if the priority queue is empty."""
        return len(self) == 0

    def __len__(self) -> int:
        """Return the number of elements in the queue."""
        return len(self._heap._data)

    

    




    

