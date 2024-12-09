class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            left = i
            # only right changes if string is even or odd
            right = i if len(s) % 2 != 0 else i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    res = s[left : right + 1]
                    resLen = right - left + 1
                left -= 1
                right += 1

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome(s="babad"))
    assert solution.longestPalindrome(s="babad") == "bab"

    print(solution.longestPalindrome(s="cbbd"))
    assert solution.longestPalindrome(s="cbbd") == "bb"
