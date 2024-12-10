from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or Selling?
        # If Buy -> i + 1
        # If Sell -> i + 2

        dp = {}  # key=(i, buying), val=max_profit

        def depth_first_search(i: int, buying: bool) -> int:
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = depth_first_search(i + 1, buying)
            if buying:
                buy = depth_first_search(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = depth_first_search(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return depth_first_search(0, True)


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit(prices=[1, 2, 3, 0, 2]))
    assert solution.maxProfit(prices=[1, 2, 3, 0, 2]) == 3

    print(solution.maxProfit(prices=[1]))
    assert solution.maxProfit(prices=[1]) == 0
