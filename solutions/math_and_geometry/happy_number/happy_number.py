from typing import Set


class Solution:
    def isHappy(self, n: int) -> bool:

        visit: Set = set()

        while n not in visit:
            if n == 1:
                return True

            visit.add(n)
            n = self.sumOfSquares(n)

        return False

    def sumOfSquares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit**2
            output += digit
            n = n // 10

        return output


if __name__ == "__main__":
    solution = Solution()
    print(solution.isHappy(n=19))
    assert solution.isHappy(n=19) == True

    print(solution.isHappy(n=2))
    assert solution.isHappy(n=2) == False
