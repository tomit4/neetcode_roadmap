from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  # (index, total) -> # of ways

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(
                i + 1, total - nums[i]
            )
            return dp[(i, total)]

        return backtrack(0, 0)


if __name__ == "__main__":
    solution = Solution()
    print(solution.findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))
    assert solution.findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3) == 5

    print(solution.findTargetSumWays(nums=[1], target=1))
    assert solution.findTargetSumWays(nums=[1], target=1) == 1
