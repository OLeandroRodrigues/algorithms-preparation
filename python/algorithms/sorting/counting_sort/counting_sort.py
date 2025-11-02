def counting_sort(arr):
    if not arr:
        return []

    k = max(arr)
    C = [0] * (k + 1)

    for value in arr:
        C[value] += 1

    for i in range(1, k + 1):
        C[i] += C[i - 1]

    B = [0] * len(arr)

    for j in range(len(arr) - 1, -1, -1):
        x = arr[j]
        C[x] -= 1          
        pos = C[x]         
        B[pos] = x

    return B



data = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(data))  # output: [1, 2, 2, 3, 3, 4, 8]