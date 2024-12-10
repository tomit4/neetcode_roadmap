class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.minDistance(word1="horse", word2="ros"))
    assert solution.minDistance(word1="horse", word2="ros") == 3

    print(solution.minDistance(word1="intention", word2="execution"))
    assert solution.minDistance(word1="intention", word2="execution") == 5
