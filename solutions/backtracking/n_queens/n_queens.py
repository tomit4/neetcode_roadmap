from typing import List, Set


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols: Set = set()
        pos_diag: Set = set()  # (r + c)
        neg_diag: Set = set()  # (r - c)
        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for col in range(n):
                if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue

                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                board[row][col] = "Q"

                backtrack(row + 1)

                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
                board[row][col] = "."

        backtrack(0)

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.solveNQueens(n=4))
    assert solution.solveNQueens(n=4) == [
        [".Q..", "...Q", "Q...", "..Q."],
        ["..Q.", "Q...", "...Q", ".Q.."],
    ]
    print(solution.solveNQueens(n=1))
    assert solution.solveNQueens(n=1) == [["Q"]]
