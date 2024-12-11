class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.checkInclusion(s1="ab", s2="eidbaooo"))
    assert solution.checkInclusion(s1="ab", s2="eidbaooo") == True

    print(solution.checkInclusion(s1="ab", s2="eidboaoo"))
    assert solution.checkInclusion(s1="ab", s2="eidboaoo") == False
