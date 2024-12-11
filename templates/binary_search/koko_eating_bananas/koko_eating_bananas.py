from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.minEatingSpeed(piles=[3, 6, 7, 11], h=8))
    assert solution.minEatingSpeed(piles=[3, 6, 7, 11], h=8) == 4

    print(solution.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))
    assert solution.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5) == 30

    print(solution.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))
    assert solution.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6) == 23
