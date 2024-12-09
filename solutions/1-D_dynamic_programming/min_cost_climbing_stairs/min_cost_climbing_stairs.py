from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [10, 15, 20] 0
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])


if __name__ == "__main__":
    solution = Solution()
    print(solution.minCostClimbingStairs(cost=[10, 15, 20]))
    assert solution.minCostClimbingStairs(cost=[10, 15, 20]) == 15

    print(solution.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
    assert (
        solution.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    )
