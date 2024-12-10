class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.uniquePaths(m=3, n=7))
    assert solution.uniquePaths(m=3, n=7) == 28

    print(solution.uniquePaths(m=3, n=2))
    assert solution.uniquePaths(m=3, n=2) == 3
