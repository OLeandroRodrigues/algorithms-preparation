# algorithms/sorting/heap_sort/heap_sort_inplace.py

from typing import List

def heapify(arr: List[int], n: int, i: int) -> None:
    
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr: List[int]) -> None:
    n = len(arr)
    # Step 1: Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements one by one
    for end in range(n - 1, 0, -1):
        # Move current root (max) to the end
        arr[0], arr[end] = arr[end], arr[0]
        # Restore heap property on reduced heap
        heapify(arr, end, 0)


if __name__ == "__main__":
    A = [7, 51, 4, 10, 15, 30, 50]
    heap_sort(A)
    print("Sorted ascending:", A)
    # Output: [4,7,10,15,30,50,51]