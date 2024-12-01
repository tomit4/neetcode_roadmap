from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left: int = 0  # left = buy
        right: int = 1  # right = sell
        max_profit: int = 0

        while right < len(prices):
            # is this a profitable transactions?
            if prices[left] < prices[right]:
                profit: int = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
            right += 1

        return max_profit


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
    print(solution.maxProfit(prices=[7, 6, 4, 3, 1]))
