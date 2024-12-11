class Solution:
    def getSum(self, a: int, b: int) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.getSum(a=1, b=2))
    assert solution.getSum(a=1, b=2) == 3

    print(solution.getSum(a=2, b=3))
    assert solution.getSum(a=2, b=3) == 5
