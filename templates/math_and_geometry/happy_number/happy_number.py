class Solution:
    def isHappy(self, n: int) -> bool:
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isHappy(n=19))
    assert solution.isHappy(n=19) == True

    print(solution.isHappy(n=2))
    assert solution.isHappy(n=2) == False
