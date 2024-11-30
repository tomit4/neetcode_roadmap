from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(solution.trap(height=[4, 2, 0, 3, 2, 5]))
