from typing import List


# Looks for duplicates, returns leftmost instance of target
def binary_search_first_occurrence(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:  # Potential result; keep searching left
            result = mid
            right = mid - 1  # Keep searching left...
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result
