class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.characterReplacement(s="ABAB", k=2))
    assert solution.characterReplacement(s="ABAB", k=2) == 4

    print(solution.characterReplacement(s="AABABBA", k=1))
    assert solution.characterReplacement(s="AABABBA", k=1) == 4
