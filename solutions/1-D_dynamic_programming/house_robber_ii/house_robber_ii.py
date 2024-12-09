from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums: List[int]):
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob

        return rob2


if __name__ == "__main__":
    solution = Solution()
    print(solution.rob(nums=[2, 3, 2]))
    assert solution.rob(nums=[2, 3, 2]) == 3

    print(solution.rob(nums=[1, 2, 3, 1]))
    assert solution.rob(nums=[1, 2, 3, 1]) == 4

    print(solution.rob(nums=[1, 2, 3]))
    assert solution.rob(nums=[1, 2, 3]) == 3
