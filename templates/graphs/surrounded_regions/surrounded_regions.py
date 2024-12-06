from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> List[List[str]]:
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
