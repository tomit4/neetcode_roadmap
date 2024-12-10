from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # O(m*n)
        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)

        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                dp[a][i] = dp[a][i + 1]
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]

        return dp[amount][0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.change(amount=5, coins=[1, 2, 5]))
    assert solution.change(amount=5, coins=[1, 2, 5]) == 4

    print(solution.change(amount=3, coins=[2]))
    assert solution.change(amount=3, coins=[2]) == 0

    print(solution.change(amount=10, coins=[10]))
    assert solution.change(amount=10, coins=[10]) == 1
