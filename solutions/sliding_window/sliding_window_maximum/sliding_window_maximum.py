import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output: List[int] = []
        queue = collections.deque()  # contains indices
        left: int = 0
        right: int = 0

        while right < len(nums):
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)

            # remove left value from window
            if left > queue[0]:
                queue.popleft()

            if (right + 1) >= k:
                output.append(nums[queue[0]])
                left += 1
            right += 1

        return output


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
    print(solution.maxSlidingWindow(nums=[1], k=1))
