# algorithms/sorting/insertion_sort/insertion_sort.py
def insertion_sort(arr):
    
    for i in range(1,len(arr)):
        
        key = arr[i] # current element
        j = i - 1

        # move the elements biggest than key from position in the front
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

    return arr