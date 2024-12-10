class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonSubsequence(text1="abcde", text2="ace"))
    assert solution.longestCommonSubsequence(text1="abcd", text2="ace") == 3

    print(solution.longestCommonSubsequence(text1="abc", text2="abc"))
    assert solution.longestCommonSubsequence(text1="abc", text2="abc") == 3

    print(solution.longestCommonSubsequence(text1="abc", text2="def"))
    assert solution.longestCommonSubsequence(text1="abc", text2="def") == 0
