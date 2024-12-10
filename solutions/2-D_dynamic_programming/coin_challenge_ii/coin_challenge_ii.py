from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # O(m*n)
        cache = {}

        def depth_first_search(i, a):
            if a == amount:
                return 1
            if a > amount:
                return 0
            if i == len(coins):
                return 0
            if (i, a) in cache:
                return cache[(i, a)]

            cache[(i, a)] = depth_first_search(i, a + coins[i]) + depth_first_search(
                i + 1, a
            )
            return cache[(i, a)]

        return depth_first_search(0, 0)


if __name__ == "__main__":
    solution = Solution()
    print(solution.change(amount=5, coins=[1, 2, 5]))
    assert solution.change(amount=5, coins=[1, 2, 5]) == 4

    print(solution.change(amount=3, coins=[2]))
    assert solution.change(amount=3, coins=[2]) == 0

    print(solution.change(amount=10, coins=[10]))
    assert solution.change(amount=10, coins=[10]) == 1
