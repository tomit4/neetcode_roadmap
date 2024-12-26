from typing import List


# NOTE: array nums is NOT guaranteed to be sorted for this
def binary_search_find_peak_element(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1

    while l < r:
        m = (l + (r - l)) // 2
        # Peak element is on the left or at mid
        if nums[m] > nums[m + 1]:
            r = m
        # Peak element is on the right of mid
        else:
            l = m + 1

    # 'l' will be the peak index when l == r
    return l
