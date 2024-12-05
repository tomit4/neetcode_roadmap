from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.letterCombinations(digits="23"))
    assert solution.letterCombinations(digits="23") == [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf",
    ]

    print(solution.letterCombinations(digits=""))
    assert solution.letterCombinations(digits="") == []

    print(solution.letterCombinations(digits="2"))
    assert solution.letterCombinations(digits="2") == ["a", "b", "c"]
