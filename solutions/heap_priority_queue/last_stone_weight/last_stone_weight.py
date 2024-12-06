import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [
            -s for s in stones
        ]  # convert all to negative in order to implement max heap
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            # if they are equal, we can do nothing, as just popping "destroys" them

            # because they are negative, the smaller stone is greater than, not less
            if second > first:
                heapq.heappush(stones, first - second)  # keeps result negative

        # edge case where stones was empty to begin with
        stones.append(0)

        return abs(stones[0])


if __name__ == "__main__":
    solution = Solution()
    print(solution.lastStoneWeight(stones=[2, 7, 4, 1, 8, 1]))
    assert solution.lastStoneWeight(stones=[2, 7, 4, 1, 8, 1]) == 1
    print(solution.lastStoneWeight(stones=[1]))
    assert solution.lastStoneWeight(stones=[1]) == 1
