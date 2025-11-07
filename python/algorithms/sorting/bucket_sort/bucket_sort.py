
def bucket_sort(arr):
    
    n = len(arr)
    if n == 0:
        return arr 

    # step 1: create n empty buckets
    buckets = [[] for _ in range(n)]

    # step 2: distribute elements into buckets based on value
    for num in arr:
        index = int(num * n)  # map value to bucket index
        if index == n:        # handle boundary case (num == 1)
            index = n - 1
        buckets[index].append(num)

    # step 3: sort each individual bucket (using insertion sort for stability)
    for bucket in buckets:
        insertion_sort(bucket)

    # step 4: concatenate all sorted buckets
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr


def insertion_sort(bucket):
    
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key


if __name__ == "__main__":
    data = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
    print("original array:", data)
    sorted_data = bucket_sort(data)
    print("sorted array:  ", sorted_data)
