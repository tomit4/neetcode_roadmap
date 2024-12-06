from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.lastStoneWeight(stones=[2, 7, 4, 1, 8, 1]))
    assert solution.lastStoneWeight(stones=[2, 7, 4, 1, 8, 1]) == 1
    print(solution.lastStoneWeight(stones=[1]))
    assert solution.lastStoneWeight(stones=[1]) == 1
