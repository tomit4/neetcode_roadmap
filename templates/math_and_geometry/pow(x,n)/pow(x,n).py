class Solution:
    def myPow(self, x: float, n: int) -> float:
        return 0.0


if __name__ == "__main__":
    solution = Solution()
    print(solution.myPow(x=2.00000, n=10))
    assert solution.myPow(x=2.00000, n=10) == 1024.00000

    print(solution.myPow(x=2.10000, n=3))
    assert solution.myPow(x=2.10000, n=3) == 9.26100

    print(solution.myPow(x=2.00000, n=-2))
    assert solution.myPow(x=2.00000, n=-2) == 0.25000
