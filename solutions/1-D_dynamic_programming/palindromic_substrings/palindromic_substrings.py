class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            # start at the same index and count odd number palindromes
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

            # reinitialize left and right pointers at i and i+1 for even number palindromes
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.countSubstrings(s="abc"))
    assert solution.countSubstrings(s="abc") == 3

    print(solution.countSubstrings(s="aaa"))
    assert solution.countSubstrings(s="aaa") == 6
