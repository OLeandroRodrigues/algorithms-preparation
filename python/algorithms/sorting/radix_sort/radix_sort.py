def counting_sort_for_radix(arr, exp):
    
    n = len(arr)
    output = [0] * n  # temporary output array
    count = [0] * 10  # for digits 0–9 (decimal base)

    # count occurrences of each digit
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    # transform count[] to represent positions (prefix sums)
    for i in range(1, 10):
        count[i] += count[i - 1]

    # build output array (traverse backwards for stability)
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # copy the output back into arr
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    if not arr:
        return

    # find the maximum number to know how many digits to process
    max_val = max(arr)
    exp = 1  # current digit place (1, 10, 100, ...)

    # sort by each digit until we've processed all digits of the largest number
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10


# ----------------------------
# example of use
# ----------------------------
if __name__ == "__main__":
    data = [329, 457, 657, 839, 436, 720, 355]
    print("Before:", data)
    radix_sort(data)
    print("After: ", data)