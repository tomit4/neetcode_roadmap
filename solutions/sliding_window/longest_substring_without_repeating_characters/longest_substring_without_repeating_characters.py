from typing import Set


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set: Set[str] = set()
        left: int = 0
        res: int = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            res = max(res, right - left + 1)

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s="abcabcbb"))
    print(solution.lengthOfLongestSubstring(s="bbbbb"))
    print(solution.lengthOfLongestSubstring(s="pwwkew"))
