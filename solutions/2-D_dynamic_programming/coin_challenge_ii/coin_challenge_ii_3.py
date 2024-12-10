from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # O(m * n) time
        # O(n) space
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP

        return dp[amount]


if __name__ == "__main__":
    solution = Solution()
    print(solution.change(amount=5, coins=[1, 2, 5]))
    assert solution.change(amount=5, coins=[1, 2, 5]) == 4

    print(solution.change(amount=3, coins=[2]))
    assert solution.change(amount=3, coins=[2]) == 0

    print(solution.change(amount=10, coins=[10]))
    assert solution.change(amount=10, coins=[10]) == 1
