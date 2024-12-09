from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
    assert solution.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]) == 4

    print(solution.lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]))
    assert solution.lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]) == 4

    print(solution.lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7]))
    assert solution.lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7]) == 1
