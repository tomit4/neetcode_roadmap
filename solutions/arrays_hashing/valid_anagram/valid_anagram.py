class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Not an anagram if both strings aren't same length
        if len(s) != len(t):
            return False

        # Build the hashmaps
        count_S, count_T = {}, {}

        for i in range(len(s)):
            count_S[s[i]] = 1 + count_S.get(s[i], 0)
            count_T[t[i]] = 1 + count_T.get(t[i], 0)

        # Checks the keys in count_S against count_T,
        # if they don't match, return False
        for c in count_S:
            if count_S[c] != count_T.get(c, 0):
                return False

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
