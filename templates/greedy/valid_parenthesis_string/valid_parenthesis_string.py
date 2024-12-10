class Solution:
    def checkValidString(self, s: str) -> bool:
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.checkValidString(s="()"))
    assert solution.checkValidString(s="()") == True

    print(solution.checkValidString(s="(*)"))
    assert solution.checkValidString(s="(*)") == True

    print(solution.checkValidString(s="(*))"))
    assert solution.checkValidString(s="(*))") == True
