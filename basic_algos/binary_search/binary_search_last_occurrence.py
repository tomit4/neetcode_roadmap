from typing import List


def binary_search_last_occurrence(arr: List[int], target: int) -> int:
    l, r = 0, len(arr) - 1
    res = -1

    while l <= r:
        m = (l + (r - l)) // 2
        if arr[m] < target:
            l = m + 1
        elif arr[m] > target:
            r = m - 1
        else:
            res = m
            # only difference between this and first occurrence
            l = m + 1

    return res
