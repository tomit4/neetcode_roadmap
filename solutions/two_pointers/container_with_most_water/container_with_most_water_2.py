from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # LINEAR TIME SOLUTION: O(n)
        res: int = 0
        left: int = 0
        right: int = len(height) - 1

        while left < right:
            area: int = (right - left) * min(height[left], height[right])
            res = max(res, area)

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                # height[left] == height[right]
                # NOTE: you could just condense this above,
                # but you could have either left +=1 or right-= 1 here
                right -= 1

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(solution.maxArea(height=[1, 1]))
