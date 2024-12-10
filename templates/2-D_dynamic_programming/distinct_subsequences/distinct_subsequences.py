class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.numDistinct(s="rabbbit", t="rabbit"))
    assert solution.numDistinct(s="rabbbit", t="rabbit") == 3

    print(solution.numDistinct(s="babgbag", t="bag"))
    assert solution.numDistinct(s="babgbag", t="bag") == 5
