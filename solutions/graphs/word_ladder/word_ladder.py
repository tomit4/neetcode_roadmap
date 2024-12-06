from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        neighbors = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                neighbors[pattern].append(word)

        visited = set([beginWord])
        queue = deque([beginWord])
        res = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for neighbor_word in neighbors[pattern]:
                        if neighbor_word not in visited:
                            visited.add(neighbor_word)
                            queue.append(neighbor_word)
            res += 1

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
