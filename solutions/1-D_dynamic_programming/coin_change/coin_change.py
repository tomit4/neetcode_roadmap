from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for amount in range(1, amount + 1):
            for coin in coins:
                if amount - coin >= 0:
                    dp[amount] = min(dp[amount], 1 + dp[amount - coin])

        return dp[amount] if dp[amount] != amount + 1 else -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.coinChange(coins=[1, 2, 5], amount=11))
    assert solution.coinChange(coins=[1, 2, 5], amount=11) == 3

    print(solution.coinChange(coins=[2], amount=3))
    assert solution.coinChange(coins=[2], amount=3) == -1

    print(solution.coinChange(coins=[1], amount=0))
    assert solution.coinChange(coins=[1], amount=0) == 0
