from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit(prices=[1, 2, 3, 0, 2]))
    assert solution.maxProfit(prices=[1, 2, 3, 0, 2]) == 3

    print(solution.maxProfit(prices=[1]))
    assert solution.maxProfit(prices=[1]) == 0
