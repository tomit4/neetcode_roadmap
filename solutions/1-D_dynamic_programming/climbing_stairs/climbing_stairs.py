class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1

        for _ in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one


if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(n=2))
    assert solution.climbStairs(n=2) == 2

    print(solution.climbStairs(n=3))
    assert solution.climbStairs(n=3) == 3
