from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow: int = 0
        fast: int = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break

        return slow


if __name__ == "__main__":
    solution = Solution()
    solution_1 = solution.findDuplicate(nums=[1, 3, 4, 2, 2])
    print(solution_1)
    solution_2 = solution.findDuplicate(nums=[3, 1, 3, 4, 2])
    print(solution_2)
    solution_3 = solution.findDuplicate(nums=[3, 3, 3, 3, 3])
    print(solution_3)
