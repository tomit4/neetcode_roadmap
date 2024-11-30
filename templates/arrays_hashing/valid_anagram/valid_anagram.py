class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram"))
    print(solution.isAnagram("rat", "car"))
