from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
    assert solution.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

    print(solution.maxArea(height=[1, 1]))
    assert solution.maxArea(height=[1, 1]) == 1
