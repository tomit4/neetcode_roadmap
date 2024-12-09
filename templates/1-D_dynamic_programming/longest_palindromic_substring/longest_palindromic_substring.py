class Solution:
    def longestPalindrome(self, s: str) -> str:
        return ""


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome(s="babad"))
    assert solution.longestPalindrome(s="babad") == "bab"

    print(solution.longestPalindrome(s="cbbd"))
    assert solution.longestPalindrome(s="cbbd") == "bb"
