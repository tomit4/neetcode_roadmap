def variable_size_sliding_window(arr, target):
    left = 0
    current_sum = 0
    min_length = float("inf")

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1

    return min_length if min_length != float("inf") else 0


# Example Problem
# Problem: Find the length of the smallest subarray with the sum >= S
arr = [2, 3, 1, 2, 4, 3]
target = 7
print(variable_size_sliding_window(arr, target))
# Output: 2 ( subarray [4, 3] has the smallest length)
