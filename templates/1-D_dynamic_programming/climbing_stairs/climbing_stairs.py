class Solution:
    def climbStairs(self, n: int) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(n=2))
    assert solution.climbStairs(n=2) == 2

    print(solution.climbStairs(n=3))
    assert solution.climbStairs(n=3) == 3
