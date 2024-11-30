from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res: List[int] = [0] * len(temperatures)
        stack: List[List[int]] = []  # pair: [temp, index]

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, stack_index = stack.pop()
                res[stack_index] = index - stack_index
            stack.append([temp, index])

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
    print(solution.dailyTemperatures(temperatures=[30, 40, 50, 60]))
    print(solution.dailyTemperatures(temperatures=[30, 60, 90]))
