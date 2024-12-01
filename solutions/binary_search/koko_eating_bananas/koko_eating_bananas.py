import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left: int = 1
        right: int = max(piles)
        res = right

        while left <= right:
            k: int = (left + right) // 2
            hours: int = 0
            for pile in piles:
                # accumulate all the hours that koko can
                # consume the bananas at given rate of k
                hours += math.ceil(pile / k)

            # if the accumulated hours is leq the passed required hours,
            # then our result is updated to take the minimum found thus far
            # and our right pointer points to an int one less than the middle (k)
            if hours <= h:
                res = min(res, k)
                right = k - 1
            # otherwise the accumulated hours is gt our passed required hours
            # and we simply move the left pointer one int  one more than the middle (k)
            else:
                left = k + 1

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.minEatingSpeed(piles=[3, 6, 7, 11], h=8))
    print(solution.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))
    print(solution.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))
