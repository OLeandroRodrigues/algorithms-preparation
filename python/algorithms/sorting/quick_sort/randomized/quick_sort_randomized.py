import random 

def quick_sort(arr, low, high):
    if low < high:
        p = randomized_partition(arr, low, high)

        quick_sort(arr, low, p - 1)     # left side
        quick_sort(arr, p + 1, high)    # right side
    
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Sample of use
if __name__ == "__main__":
    A = [2, 8, 7, 1, 3, 5, 6]
    print("Before:", A)
    quick_sort(A, 0, len(A) - 1)
    print("After:", A)