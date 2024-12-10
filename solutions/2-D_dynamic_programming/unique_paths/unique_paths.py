class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for _ in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow

        return row[0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.uniquePaths(m=3, n=7))
    assert solution.uniquePaths(m=3, n=7) == 28

    print(solution.uniquePaths(m=3, n=2))
    assert solution.uniquePaths(m=3, n=2) == 3
