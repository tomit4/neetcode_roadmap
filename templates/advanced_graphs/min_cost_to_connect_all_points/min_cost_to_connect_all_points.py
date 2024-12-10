from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.minCostConnectPoints(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]])
    )
    assert (
        solution.minCostConnectPoints(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]])
        == 20
    )

    print(solution.minCostConnectPoints(points=[[3, 12], [-2, 5], [-4, 1]]))
    assert solution.minCostConnectPoints(points=[[3, 12], [-2, 5], [-4, 1]]) == 18
