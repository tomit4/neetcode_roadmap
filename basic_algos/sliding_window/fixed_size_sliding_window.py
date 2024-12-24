def fixed_size_sliding_window(arr, k):
    if len(arr) < k:
        return []  # Handle edge case where window size exceeds array length

    result = []
    window_sum = 0

    # Initialize the first window
    for i in range(k):
        window_sum += arr[i]
    result.append(window_sum)

    # Slide the window
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        result.append(window_sum)

    return result


# Example Problem
# Problem: Given an array, find the sum of all subarrays of size k.

arr = [1, 2, 3, 4, 5]
k = 3
print(fixed_size_sliding_window(arr, k))
# Output: [6, 9, 12]
