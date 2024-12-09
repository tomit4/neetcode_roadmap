from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.coinChange(coins=[1, 2, 5], amount=11))
    assert solution.coinChange(coins=[1, 2, 5], amount=11) == 3

    print(solution.coinChange(coins=[2], amount=3))
    assert solution.coinChange(coins=[2], amount=3) == -1

    print(solution.coinChange(coins=[1], amount=0))
    assert solution.coinChange(coins=[1], amount=0) == 0
