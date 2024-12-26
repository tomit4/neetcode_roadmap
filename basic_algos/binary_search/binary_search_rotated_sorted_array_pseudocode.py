from typing import List


def left_ptr_has_not_passed_or_met_right_ptr(left_ptr: int, right_ptr: int) -> bool:
    return left_ptr <= right_ptr


def target_is_found(nums: List[int], mid_ptr: int, target: int) -> bool:
    return nums[mid_ptr] == target


def left_side_of_array_is_sorted(nums: List[int], left_ptr: int, mid_ptr: int) -> bool:
    return nums[left_ptr] <= nums[mid_ptr]


def target_is_between_left_ptr_and_mid_ptr(
    nums: List[int], left_ptr: int, mid_ptr: int, target: int
) -> bool:
    return nums[left_ptr] <= target < nums[mid_ptr]


def target_is_between_mid_ptr_and_right_ptr(
    nums: List[int], right_ptr: int, mid_ptr: int, target: int
) -> bool:
    return nums[mid_ptr] < target <= nums[right_ptr]


def binary_search_rotated_sorted_array(nums: List[int], target: int) -> int:
    left_ptr, right_ptr = 0, len(nums) - 1

    left_has_not_passed_or_met_right = left_ptr_has_not_passed_or_met_right_ptr(
        left_ptr, right_ptr
    )

    while left_has_not_passed_or_met_right:
        mid_ptr = (left_ptr + (right_ptr - left_ptr)) // 2
        target_found = target_is_found(nums, mid_ptr, target)

        if target_found:
            return mid_ptr

        left_side_is_sorted = left_side_of_array_is_sorted(nums, left_ptr, mid_ptr)
        right_side_is_sorted = not left_side_is_sorted
        target_is_between_left_and_mid = target_is_between_left_ptr_and_mid_ptr(
            nums, left_ptr, mid_ptr, target
        )
        target_is_between_mid_and_right = target_is_between_mid_ptr_and_right_ptr(
            nums, right_ptr, mid_ptr, target
        )

        if left_side_is_sorted:
            if target_is_between_left_and_mid:
                left_ptr = mid_ptr + 1
            else:
                right_ptr = mid_ptr - 1
        elif right_side_is_sorted:
            if target_is_between_mid_and_right:
                right_ptr = mid_ptr - 1
            else:
                left_ptr = mid_ptr + 1

    return -1
