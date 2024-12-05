from typing import Dict, List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res: List[str] = []
        digit_to_char: Dict[str, str] = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i: int, cur_str: str):
            if len(cur_str) == len(digits):
                res.append(cur_str)
                return

            for c in digit_to_char[digits[i]]:
                backtrack(i + 1, cur_str + c)

        if len(digits):
            backtrack(0, "")

        return res


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
