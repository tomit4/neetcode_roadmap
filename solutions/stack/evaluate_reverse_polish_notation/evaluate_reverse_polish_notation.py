from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[int] = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a: int = stack.pop()
                b: int = stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a: int = stack.pop()
                b: int = stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))

        return stack[0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.evalRPN(tokens=["2", "1", "+", "3", "*"]))
    print(solution.evalRPN(tokens=["4", "13", "5", "/", "+"]))
    print(
        solution.evalRPN(
            tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        )
    )
