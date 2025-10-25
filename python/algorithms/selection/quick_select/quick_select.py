import random

def quick_select(arr, low, high, k):

    if k < 1 or k > (high - low + 1):
        raise IndexError("k out of range")
    
    if low == high:
        return arr[low] 
    
    if low < high:
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high]  = arr[high],arr[pivot_index] 
        p = partition(arr, low, high)

        pos = p - low + 1
        if pos == k: 
            return arr[p] 
        elif pos > k:
            return quick_select(arr, low, p -1, k)
        else:
            return quick_select(arr, p + 1, high, k - pos) 

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage
'''if __name__ == "__main__":
    nums = [7, 10, 4, 3, 20, 15]
    k = 3
    result = quick_select(nums, 0, len(nums) - 1, k)
    print(f"{k}-th smallest element is {result}")'''