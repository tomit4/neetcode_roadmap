from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.canJump(nums=[2, 3, 1, 1, 4]))
    assert solution.canJump(nums=[2, 3, 1, 1, 4]) == True

    print(solution.canJump(nums=[3, 2, 1, 0, 4]))
    assert solution.canJump(nums=[3, 2, 1, 0, 4]) == False
