from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestIncreasingPath(matrix=[[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
    assert solution.longestIncreasingPath(matrix=[[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4

    print(solution.longestIncreasingPath(matrix=[[3, 4, 5], [3, 2, 6], [2, 2, 1]]))
    assert solution.longestIncreasingPath(matrix=[[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4

    print(solution.longestIncreasingPath(matrix=[[1]]))
    assert solution.longestIncreasingPath(matrix=[[1]]) == 1
