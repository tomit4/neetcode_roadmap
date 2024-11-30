from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return [[""]]


if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(solution.groupAnagrams(strs=[""]))
    print(solution.groupAnagrams(strs=["a"]))
