from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.ladderLength(
            beginWord="hit",
            endWord="cog",
            wordList=["hot", "dot", "dog", "lot", "log", "cog"],
        )
    )
    assert (
        solution.ladderLength(
            beginWord="hit",
            endWord="cog",
            wordList=["hot", "dot", "dog", "lot", "log", "cog"],
        )
        == 5
    )

    print(
        solution.ladderLength(
            beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"]
        )
    )
    assert (
        solution.ladderLength(
            beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"]
        )
        == 0
    )
