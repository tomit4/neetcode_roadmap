from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    assert solution.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    print(solution.maxSubArray(nums=[1]))
    assert solution.maxSubArray(nums=[1]) == 1

    print(solution.maxSubArray(nums=[5, 4, -1, 7, 8]))
    assert solution.maxSubArray(nums=[5, 4, -1, 7, 8]) == 23
