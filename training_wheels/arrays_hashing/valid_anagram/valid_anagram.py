# check if the two strings are equal first, if not, return False
# establish two hashmaps
# iterate once over the string
# populate the hash maps with the count of each character
# use the dicitonary .get() method with an initializer of 0 to increment

# iterate over the count map of s string
# if the amount found at each element in the map doesn't equal the amount found in the count t map, then return False
# after the loop return True


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
