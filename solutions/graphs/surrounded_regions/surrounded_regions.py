from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> List[List[str]]:
        ROWS = len(board)
        COLS = len(board[0])

        # DFS
        def capture(row, col):
            if (
                row < 0
                or col < 0
                or row == ROWS
                or col == COLS
                or board[row][col] != "O"
            ):
                return

            board[row][col] = "T"
            capture(row + 1, col)
            capture(row - 1, col)
            capture(row, col + 1)
            capture(row, col - 1)

        # 1. (DFS) Capture unsurrounded regions (O -> T)
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O" and (
                    row in [0, ROWS - 1] or col in [0, COLS - 1]
                ):
                    capture(row, col)

        # 2. Capture the surrounded regions (O -> X)
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"

        # 3. Uncapture unsurrounded regions (T - O)
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "T":
                    board[row][col] = "O"

        return board


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.solve(
            board=[
                ["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"],
            ]
        )
    )
    assert solution.solve(
        board=[
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
    ) == [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]

    print(solution.solve(board=[["X"]]))
    assert solution.solve(board=[["X"]]) == [["X"]]
