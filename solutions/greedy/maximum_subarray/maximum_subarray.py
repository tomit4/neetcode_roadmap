from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        cur_sum = 0

        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            max_sub = max(max_sub, cur_sum)

        return max_sub


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    assert solution.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    print(solution.maxSubArray(nums=[1]))
    assert solution.maxSubArray(nums=[1]) == 1

    print(solution.maxSubArray(nums=[5, 4, -1, 7, 8]))
    assert solution.maxSubArray(nums=[5, 4, -1, 7, 8]) == 23
