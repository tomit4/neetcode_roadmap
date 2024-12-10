class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isMatch(s="aa", p="a"))
    assert solution.isMatch(s="aa", p="a") == False

    print(solution.isMatch(s="aa", p="a*"))
    assert solution.isMatch(s="aa", p="a*") == True

    print(solution.isMatch(s="ab", p=".*"))
    assert solution.isMatch(s="ab", p=".*") == True
