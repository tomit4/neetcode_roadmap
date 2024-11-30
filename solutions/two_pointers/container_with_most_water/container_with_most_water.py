from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # BRUTE FORCE
        res: int = 0

        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                area: int = (right - left) * min(height[left], height[right])
                res = max(res, area)

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(solution.maxArea(height=[1, 1]))
