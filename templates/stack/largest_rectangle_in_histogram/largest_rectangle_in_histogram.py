from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.largestRectangleArea(heights=[2, 1, 5, 6, 2, 3]))
    assert solution.largestRectangleArea(heights=[2, 1, 5, 6, 2, 3]) == 10

    print(solution.largestRectangleArea(heights=[2, 4]))
    assert solution.largestRectangleArea(heights=[2, 4]) == 4
