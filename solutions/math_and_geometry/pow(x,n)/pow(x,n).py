class Solution:

    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = helper(x, n // 2)
            res = res * res
            return x * res if n % 2 else res

        res = helper(x, abs(n))
        return round(res if n >= 0 else 1 / res, 5)


if __name__ == "__main__":
    solution = Solution()
    print(solution.myPow(x=2.00000, n=10))
    assert solution.myPow(x=2.00000, n=10) == 1024.00000

    print(solution.myPow(x=2.10000, n=3))
    assert solution.myPow(x=2.10000, n=3) == 9.26100

    print(solution.myPow(x=2.00000, n=-2))
    assert solution.myPow(x=2.00000, n=-2) == 0.25000
