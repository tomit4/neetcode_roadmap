from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area: int = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start: int = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area


if __name__ == "__main__":
    solution = Solution()
    print(solution.largestRectangleArea(heights=[2, 1, 5, 6, 2, 3]))
    print(solution.largestRectangleArea(heights=[2, 4]))
