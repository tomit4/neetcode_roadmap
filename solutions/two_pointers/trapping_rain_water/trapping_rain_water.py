from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left: int = 0
        right: int = len(height) - 1
        left_max: int = height[left]
        right_max: int = height[right]
        res: int = 0

        while left < right:
            if left_max < right_max:
                left += 1
                # NOTE: due to max being calculated before adding to
                # res, left_max - height[left] will never be a negative number
                left_max = max(left_max, height[left])
                res += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                res += right_max - height[right]

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(solution.trap(height=[4, 2, 0, 3, 2, 5]))
