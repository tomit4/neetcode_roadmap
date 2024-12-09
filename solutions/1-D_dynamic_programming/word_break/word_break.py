from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True  # out of bounds is True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i : i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break

        return dp[0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.wordBreak(s="leetcode", wordDict=["leet", "code"]))
    assert solution.wordBreak(s="leetcode", wordDict=["leet", "code"]) == True

    print(solution.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
    assert solution.wordBreak(s="applepenapple", wordDict=["apple", "pen"]) == True

    print(
        solution.wordBreak(
            s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]
        )
    )
    assert (
        solution.wordBreak(
            s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]
        )
        == False
    )
