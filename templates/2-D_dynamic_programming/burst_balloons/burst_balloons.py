from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxCoins(nums=[3, 1, 5, 8]))
    assert solution.maxCoins(nums=[3, 1, 5, 8]) == 167

    print(solution.maxCoins(nums=[1, 5]))
    assert solution.maxCoins(nums=[1, 5]) == 10
