class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time complexity is likely O(nlogn),
        # which is less efficient than valid_anagram.py solution
        return sorted(s) == sorted(t)


if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram"))
    print(solution.isAnagram("rat", "car"))
