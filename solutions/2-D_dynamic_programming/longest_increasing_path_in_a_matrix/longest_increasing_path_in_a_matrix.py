from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}  # (r, c) -> LIP

        def depth_first_serach(row, col, prev_val):
            if (
                row < 0
                or row == ROWS
                or col < 0
                or col == COLS
                or matrix[row][col] <= prev_val
            ):
                return 0
            if (row, col) in dp:
                return dp[(row, col)]

            res = 1
            res = max(res, 1 + depth_first_serach(row + 1, col, matrix[row][col]))
            res = max(res, 1 + depth_first_serach(row - 1, col, matrix[row][col]))
            res = max(res, 1 + depth_first_serach(row, col + 1, matrix[row][col]))
            res = max(res, 1 + depth_first_serach(row, col - 1, matrix[row][col]))

            dp[(row, col)] = res
            return res

        for row in range(ROWS):
            for col in range(COLS):
                depth_first_serach(row, col, -1)

        return max(dp.values())


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestIncreasingPath(matrix=[[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
    assert solution.longestIncreasingPath(matrix=[[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4

    print(solution.longestIncreasingPath(matrix=[[3, 4, 5], [3, 2, 6], [2, 2, 1]]))
    assert solution.longestIncreasingPath(matrix=[[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4

    print(solution.longestIncreasingPath(matrix=[[1]]))
    assert solution.longestIncreasingPath(matrix=[[1]]) == 1
