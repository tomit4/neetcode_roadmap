from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.change(amount=5, coins=[1, 2, 5]))
    assert solution.change(amount=5, coins=[1, 2, 5]) == 4

    print(solution.change(amount=3, coins=[2]))
    assert solution.change(amount=3, coins=[2]) == 0

    print(solution.change(amount=10, coins=[10]))
    assert solution.change(amount=10, coins=[10]) == 1
