class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s="abcabcbb"))
    assert solution.lengthOfLongestSubstring(s="abcabcbb") == 3

    print(solution.lengthOfLongestSubstring(s="bbbbb"))
    assert solution.lengthOfLongestSubstring(s="bbbbb") == 1

    print(solution.lengthOfLongestSubstring(s="pwwkew"))
    assert solution.lengthOfLongestSubstring(s="pwwkew") == 3
