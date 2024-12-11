from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
    assert solution.maxProfit(prices=[7, 1, 5, 3, 6, 4]) == 5

    print(solution.maxProfit(prices=[7, 6, 4, 3, 1]))
    assert solution.maxProfit(prices=[7, 6, 4, 3, 1]) == 0
