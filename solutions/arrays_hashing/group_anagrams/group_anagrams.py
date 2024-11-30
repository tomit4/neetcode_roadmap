from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26  # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())

    # Time Complexity: O(m * n) where m is the number of strings
    # and n is the average number of characters in each string


if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(solution.groupAnagrams(strs=[""]))
    print(solution.groupAnagrams(strs=["a"]))
