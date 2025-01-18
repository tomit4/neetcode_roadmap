from collections import defaultdict
from typing import List


class Solution_2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            # causes time complexity to be (m * n * log(n)) where m is num of strings and n is avg num of characters in str
            sorted_str = "".join(sorted(s))
            if sorted_str not in res:
                res[sorted_str] = []

            res[sorted_str].append(s)

        return list(res.values())


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

    assert solution.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["eat", "tea", "ate"],
        ["tan", "nat"],
        ["bat"],
    ]

    print(solution.groupAnagrams(strs=[""]))
    assert solution.groupAnagrams(strs=[""]) == [[""]]

    print(solution.groupAnagrams(strs=["a"]))
    assert solution.groupAnagrams(strs=["a"]) == [["a"]]
