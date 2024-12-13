class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram(s="anagram", t="nagaram"))
    assert solution.isAnagram(s="anagram", t="nagaram") == True
    print(solution.isAnagram(s="nagaram", t="anagramm"))
    assert solution.isAnagram(s="nagaram", t="anagramm") == False
    print(solution.isAnagram(s="rat", t="car"))
    assert solution.isAnagram(s="rat", t="car") == False
    print(solution.isAnagram(s="a", t="ab"))
    assert solution.isAnagram(s="a", t="ab") == False
    print(solution.isAnagram(s="ab", t="a"))
    assert solution.isAnagram(s="ab", t="a") == False
