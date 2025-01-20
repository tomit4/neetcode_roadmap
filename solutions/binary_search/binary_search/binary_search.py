from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left: int = 0
        right: int = len(nums) - 1

        while left <= right:
            #  mid: int = (left + right) // 2 # more straight forward way of finding mid
            mid: int = left + (
                (right - left) // 2
            )  # never causes overflow in other langs like C
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.search(nums=[-1, 0, 3, 5, 9, 12], target=9))
    assert solution.search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4

    print(solution.search(nums=[-1, 0, 3, 5, 9, 12], target=2))
    assert solution.search(nums=[-1, 0, 3, 5, 9, 12], target=2) == -1

    print(solution.search(nums=[-1, 0, 3, 5, 9, 12], target=0))
    assert solution.search(nums=[-1, 0, 3, 5, 9, 12], target=0) == 1
