from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return [0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
    assert solution.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3) == [
        3,
        3,
        5,
        5,
        6,
        7,
    ]

    print(solution.maxSlidingWindow(nums=[1], k=1))
    assert solution.maxSlidingWindow(nums=[1], k=1) == [1]
