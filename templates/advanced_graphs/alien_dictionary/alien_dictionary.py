from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        return ""


if __name__ == "__main__":
    solution = Solution()
    print(solution.foreignDictionary(words=["z", "o"]))
    assert solution.foreignDictionary(words=["z", "o"]) == "zo"

    print(solution.foreignDictionary(words=["hrn", "hrf", "er", "enn", "rfnn"]))
    assert (
        solution.foreignDictionary(words=["hrn", "hrf", "er", "enn", "rfnn"]) == "hernf"
    )
