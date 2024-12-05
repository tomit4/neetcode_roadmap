from typing import List, Set


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS: int = len(board)
        COLS: int = len(board[0])
        path: Set = set()

        def depth_first_search(row, col, i):
            if i == len(word):
                return True

            if (
                row < 0
                or col < 0
                or row >= ROWS
                or col >= COLS
                or word[i] != board[row][col]
                or (row, col) in path
            ):
                return False

            path.add((row, col))

            res = (
                depth_first_search(row + 1, col, i + 1)
                or depth_first_search(row - 1, col, i + 1)
                or depth_first_search(row, col + 1, i + 1)
                or depth_first_search(row, col - 1, i + 1)
            )

            path.remove((row, col))

            return res

        for row in range(ROWS):
            for col in range(COLS):
                if depth_first_search(row, col, 0):
                    return True

        return False

    # O(n * m * 4^n) where n is the amount of characters in word


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.exist(
            board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            word="ABCCED",
        )
    )
    assert (
        solution.exist(
            board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            word="ABCCED",
        )
        == True
    )
    print(
        solution.exist(
            board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            word="SEE",
        )
    )
    assert (
        solution.exist(
            board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            word="SEE",
        )
        == True
    )
    print(
        solution.exist(
            board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            word="ABCB",
        )
    )
    assert (
        solution.exist(
            board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            word="ABCB",
        )
        == True
    )
