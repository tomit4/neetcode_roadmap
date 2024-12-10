from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))
    assert solution.findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3) == 5

    print(solution.findTargetSumWays(nums=[1], target=1))
    assert solution.findTargetSumWays(nums=[1], target=1) == 1
