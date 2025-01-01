from math import ceil
from typing import List


# Another solution found on math.stackexchange
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = max(piles)

        l, r = min_speed, max_speed
        while l < r:
            mid_speed = (l + r) // 2
            hours_needed = sum(ceil(pile / mid_speed) for pile in piles)
            if hours_needed <= h:
                r = mid_speed
            else:  # t > h
                l = mid_speed + 1

        return l


# NOTE: Not Neetcode's solution, took a hybrid approach with this one,
# some of this is his, some of this is another solution found on Leetcode site
# note that binary search *lower bound* is indicative of this solution
class Solution_1:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min number of bananas koko can eat in an hour
        left: int = 1
        # max number of bananas koko can eat in an hour
        right: int = max(piles)

        def hours_needed(k):
            hours_needed = 0
            for pile in piles:
                hours_needed += ceil(pile / k)
            return hours_needed

        while left < right:
            k: int = (left + right) // 2
            if hours_needed(k) <= h:
                right = k
            else:
                left = k + 1

        return left


if __name__ == "__main__":
    solution = Solution()
    print(solution.minEatingSpeed(piles=[3, 6, 7, 11], h=8))
    print(solution.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))
    print(solution.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))
