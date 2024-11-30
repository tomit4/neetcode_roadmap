from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.evalRPN(tokens=["2", "1", "+", "3", "*"]))
    print(solution.evalRPN(tokens=["4", "13", "5", "/", "+"]))
    print(
        solution.evalRPN(
            tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        )
    )
