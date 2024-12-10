from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}

        def depth_first_search(left, right):
            if left > right:
                return 0
            if (left, right) in dp:
                return dp[(left, right)]

            dp[(left, right)] = 0
            for i in range(left, right + 1):
                coins = nums[left - 1] * nums[i] * nums[right + 1]
                coins += depth_first_search(left, i - 1) + depth_first_search(
                    i + 1, right
                )
                dp[(left, right)] = max(dp[(left, right)], coins)
            return dp[(left, right)]

        return depth_first_search(1, len(nums) - 2)


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxCoins(nums=[3, 1, 5, 8]))
    assert solution.maxCoins(nums=[3, 1, 5, 8]) == 167

    print(solution.maxCoins(nums=[1, 5]))
    assert solution.maxCoins(nums=[1, 5]) == 10
