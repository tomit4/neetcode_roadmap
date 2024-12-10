class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonSubsequence(text1="abcde", text2="ace"))
    assert solution.longestCommonSubsequence(text1="abcde", text2="ace") == 3

    print(solution.longestCommonSubsequence(text1="abc", text2="abc"))
    assert solution.longestCommonSubsequence(text1="abc", text2="abc") == 3

    print(solution.longestCommonSubsequence(text1="abc", text2="def"))
    assert solution.longestCommonSubsequence(text1="abc", text2="def") == 0
