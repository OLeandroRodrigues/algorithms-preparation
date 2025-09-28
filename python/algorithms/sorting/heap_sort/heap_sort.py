# My idea was to use the heap class that I built from scratch 

# algorithms/sorting/heap_sort/heap_sort.py

from typing import List
from data_structures.heap.max_heap import MaxHeap


class HeapSort:
    """
    HeapSort implementation reusing the existing MaxHeap.
    - sort_asc: returns ascending order
    - sort_desc: returns descending order
    Note: returns a NEW list (does not mutate the input).
    """

    @staticmethod
    def sort_desc(arr: List[int]) -> List[int]:
        """
        Sorts in descending order by reusing MaxHeap:
        inserts all elements and repeatedly pops the max (largest -> smallest).
        """
        heap = MaxHeap()
        for item in arr:
            heap.insert(item)
        return [heap.pop() for _ in range(len(arr))]

    @staticmethod
    def sort_asc(arr: List[int]) -> List[int]:
        """
        Sorts in ascending order using the same MaxHeap:
        obtains the descending list and then reverses it.
        """
        desc = HeapSort.sort_desc(arr)
        return list(reversed(desc))


if __name__ == "__main__":
    A = [4, 5, 5, 10, 10, 8, 2, 100, 50, 30, 1]
    print("Asc :", HeapSort.sort_asc(A))   # [1, 2, 4, 5, 5, 8, 10, 10, 30, 50, 100]
    print("Desc:", HeapSort.sort_desc(A))  # [100, 50, 30, 10, 10, 8, 5, 5, 4, 2, 1]