class Solution:
    def countSubstrings(self, s: str) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.countSubstrings(s="abc"))
    assert solution.countSubstrings(s="abc") == 3

    print(solution.countSubstrings(s="aaa"))
    assert solution.countSubstrings(s="aaa") == 6
