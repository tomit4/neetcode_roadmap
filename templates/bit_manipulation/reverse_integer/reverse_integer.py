class Solution:
    def reverse(self, x: int) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(x=123))
    assert solution.reverse(x=123) == 321

    print(solution.reverse(x=-123))
    assert solution.reverse(x=-123) == -321

    print(solution.reverse(x=120))
    assert solution.reverse(x=120) == 21
