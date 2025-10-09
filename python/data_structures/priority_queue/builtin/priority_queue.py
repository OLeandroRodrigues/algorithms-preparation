# python/data_structures/priority_queue/builtin/priority_queue.py
from __future__ import annotations

import heapq
import itertools
from typing import Any, List, Tuple


class PriorityQueue:
    """Priority Queue implemented with Python's built-in heapq (binary min-heap).

    Stability:
        Uses a monotonically increasing counter (order) to keep FIFO behavior among
        elements with the same priority. We store tuples (eff_priority, order, value).

    Min vs Max behavior:
        - For min-priority behavior (default), eff_priority = priority
        - For max-priority behavior, eff_priority = -priority

    Operations:
        - push(value, priority): O(log n)
        - pop(): O(log n)
        - peek(): O(1)
        - is_empty(), __len__(): O(1)
    """

    def __init__(self, *, is_min: bool = True) -> None:
        """Initialize an empty priority queue.

        Args:
            is_min (bool): If True (default), smaller priorities come out first.
                           If False, behaves like a max-priority queue.
        """
        self._heap: List[Tuple[int, int, Any]] = []
        self._is_min = is_min
        self._order = itertools.count() 

    def push(self, value: Any, priority: int) -> None:
        """Insert a new element with a given priority.

        Args:
            value: Payload value to store.
            priority: Logical priority associated with the value.
        """
        order = next(self._order)
        eff_priority = priority if self._is_min else -priority
        # Tuple order defines comparison: first by eff_priority, then by order (FIFO), then value if needed
        heapq.heappush(self._heap, (eff_priority, order, value))

    def pop(self) -> Any:
        """Remove and return the value with highest priority according to is_min.

        Raises:
            IndexError: If the queue is empty.
        """
        if not self._heap:
            raise IndexError("pop from an empty priority queue")
        eff_priority, order, value = heapq.heappop(self._heap)
        return value

    def peek(self) -> Any:
        """Return the next value without removing it.

        Raises:
            IndexError: If the queue is empty.
        """
        if not self._heap:
            raise IndexError("peek from an empty priority queue")
        eff_priority, order, value = self._heap[0]
        return value

    def __len__(self) -> int:
        """Return current number of elements."""
        return len(self._heap)

    def is_empty(self) -> bool:
        """Return True if the queue has no elements."""
        return not self._heap