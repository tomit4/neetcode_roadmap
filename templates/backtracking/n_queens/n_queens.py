from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
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
