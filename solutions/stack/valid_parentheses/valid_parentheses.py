from typing import Dict, List


class Solution:
    def isValid(self, s: str) -> bool:
        stack: List[str] = []
        close_to_open: Dict[str, str] = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in close_to_open:
                # if the stack is not empty and
                # the stack's peek is equal to it's closing character
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid(s="()"))
    print(solution.isValid(s="()[]{}"))
    print(solution.isValid(s="(]"))
    print(solution.isValid(s="([])"))
