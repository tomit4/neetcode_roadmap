from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return True


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
