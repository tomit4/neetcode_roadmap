from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
    assert solution.dailyTemperatures(
        temperatures=[73, 74, 75, 71, 69, 72, 76, 73]
    ) == [1, 1, 4, 2, 1, 1, 0, 0]

    print(solution.dailyTemperatures(temperatures=[30, 40, 50, 60]))
    assert solution.dailyTemperatures(temperatures=[30, 40, 50, 60]) == [1, 1, 1, 0]

    print(solution.dailyTemperatures(temperatures=[30, 60, 90]))
    assert solution.dailyTemperatures(temperatures=[30, 60, 90]) == [1, 1, 0]
