from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.minCostClimbingStairs(cost=[10, 15, 20]))
    assert solution.minCostClimbingStairs(cost=[10, 15, 20]) == 15

    print(solution.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
    assert (
        solution.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    )
