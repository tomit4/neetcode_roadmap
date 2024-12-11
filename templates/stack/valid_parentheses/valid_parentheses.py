class Solution:
    def isValid(self, s: str) -> bool:
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid(s="()"))
    assert solution.isValid(s="()") == True

    print(solution.isValid(s="()[]{}"))
    assert solution.isValid(s="()[]{}") == True

    print(solution.isValid(s="(]"))
    assert solution.isValid(s="(]") == False

    print(solution.isValid(s="([])"))
    assert solution.isValid(s="([])") == True
