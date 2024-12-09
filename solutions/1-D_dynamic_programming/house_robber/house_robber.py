from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2


if __name__ == "__main__":
    solution = Solution()
    print(solution.rob(nums=[1, 2, 3, 1]))
    assert solution.rob(nums=[1, 2, 3, 1]) == 4

    print(solution.rob(nums=[2, 7, 9, 3, 1]))
    assert solution.rob(nums=[2, 7, 9, 3, 1]) == 12
