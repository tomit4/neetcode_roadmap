from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return True


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
