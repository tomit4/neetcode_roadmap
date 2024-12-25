from typing import List


# More explicitly demonstrates what is happening
def binary_search_find_target_in_sorted_array_explicit(arr: List[int], target: int):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            return mid

    return -1


def binary_search_find_target_in_sorted_array(arr: List[int], target: int):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:  # Found target
            return mid
        elif arr[mid] < target:  # Target is in the right half
            left = mid + 1
        else:  # Target is in the left half
            right = mid - 1
    return -1  # Target not found
