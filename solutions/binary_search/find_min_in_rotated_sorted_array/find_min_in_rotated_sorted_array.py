from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res: int = nums[0]
        left: int = 0
        right: int = len(nums) - 1

        while left <= right:
            # if the array is sorted
            # (or we have found a subsection of the array that is sorted)
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            # establish a mid pointer, reassign res to the min of the two
            mid: int = (left + right) // 2
            res = min(res, nums[mid])
            # if the mid is greater than left, then the
            # current mid is part of the left subsection
            if nums[mid] >= nums[left]:
                left = mid + 1
            # else the mid is part of the right subsection
            else:
                right = mid - 1

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMin(nums=[3, 4, 5, 1, 2]))
    assert solution.findMin(nums=[3, 4, 5, 1, 2]) == 1
    print(solution.findMin(nums=[4, 5, 6, 7, 0, 1, 2]))
    assert solution.findMin(nums=[4, 5, 6, 7, 0, 1, 2]) == 0
    print(solution.findMin(nums=[11, 13, 15, 17]))
    assert solution.findMin(nums=[11, 13, 15, 17]) == 11
    print(solution.findMin(nums=[1]))
    assert solution.findMin(nums=[1]) == 1
    print(solution.findMin(nums=[2, 3, 4, 5, 1]))
    assert solution.findMin(nums=[2, 3, 4, 5, 1]) == 1
