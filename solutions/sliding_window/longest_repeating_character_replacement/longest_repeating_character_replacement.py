from typing import Dict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count: Dict[str, int] = {}  # counts occurrences of each character
        res: int = 0

        left: int = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.characterReplacement(s="ABAB", k=2))
    print(solution.characterReplacement(s="AABABBA", k=1))
