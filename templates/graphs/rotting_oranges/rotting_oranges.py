from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
    assert solution.orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4

    print(solution.orangesRotting(grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
    assert solution.orangesRotting(grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1

    print(solution.orangesRotting(grid=[[0, 2]]))
    assert solution.orangesRotting(grid=[[0, 2]]) == 0
