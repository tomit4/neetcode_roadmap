from typing import List


# create a variable called res and assign it a defaultdict of a list type
# iterate over the strs array
# establish a count array of 26 zeroes
# create an inner for loop that iterates over the characters of the string
# using the ord() method, at the count index of the ord of c minus the ord of the character "a", increment that value by 1
# at the res index of a tuple of count, append s
# return the values of res converted to a list
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return [[""]]


if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
    assert solution.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["bat"],
        ["nat", "tan"],
        ["ate", "eat", "tea"],
    ]

    print(solution.groupAnagrams(strs=[""]))
    assert solution.groupAnagrams(strs=[""]) == [[""]]

    print(solution.groupAnagrams(strs=["a"]))
    assert solution.groupAnagrams(strs=["a"]) == [["a"]]
