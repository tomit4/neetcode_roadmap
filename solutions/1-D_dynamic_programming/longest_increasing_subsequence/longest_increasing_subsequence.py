from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
    assert solution.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]) == 4

    print(solution.lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]))
    assert solution.lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]) == 4

    print(solution.lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7]))
    assert solution.lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7]) == 1
