class Solution:
    def myPow(self, x: float, n: int) -> float:
        # ChatGPT
        res = 1
        abs_n = abs(n)

        while abs_n:
            if abs_n % 2:
                res *= x
            x *= x
            abs_n //= 2

        return round(res if n >= 0 else 1 / res, 5)


if __name__ == "__main__":
    solution = Solution()
    print(solution.myPow(x=2.00000, n=10))
    assert solution.myPow(x=2.00000, n=10) == 1024.00000

    print(solution.myPow(x=2.10000, n=3))
    assert solution.myPow(x=2.10000, n=3) == 9.26100

    print(solution.myPow(x=2.00000, n=-2))
    assert solution.myPow(x=2.00000, n=-2) == 0.25000
