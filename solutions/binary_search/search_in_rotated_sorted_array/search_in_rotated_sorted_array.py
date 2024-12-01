from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left: int = 0
        right: int = len(nums) - 1

        while left <= right:
            mid: int = (left + right) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[left] <= nums[mid]:
                # target must be in right most portion
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                # target must be in left most portion
                else:
                    right = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
    print(solution.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
    print(solution.search(nums=[1], target=0))
