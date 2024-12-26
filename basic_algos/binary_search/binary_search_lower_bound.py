from typing import List


# Find the first index where target could be inserted
# in order to maintain order of arr.
def binary_search_lower_bound(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    result = len(arr)

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:  # Possible candidate
            result = mid
            right = mid - 1  # Look for smaller valid candidates
        else:
            left = mid + 1

    return result
