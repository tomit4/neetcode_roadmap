from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        return []


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.findWords(
            board=[
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            words=["oath", "pea", "eat", "rain"],
        )
    )
    # NOTE: Cast to `set` since it can output both words in either order
    assert set(
        solution.findWords(
            board=[
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            words=["oath", "pea", "eat", "rain"],
        )
    ) == {"eat", "oath"}
    print(solution.findWords(board=[["a", "b"], ["c", "d"]], words=["abcb"]))
    assert solution.findWords(board=[["a", "b"], ["c", "d"]], words=["abcb"]) == []
