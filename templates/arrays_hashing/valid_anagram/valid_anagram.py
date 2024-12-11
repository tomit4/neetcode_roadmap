class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram"))
    assert solution.isAnagram("anagram", "nagaram") == True
    print(solution.isAnagram("rat", "car"))
    assert solution.isAnagram("rat", "car") == False
