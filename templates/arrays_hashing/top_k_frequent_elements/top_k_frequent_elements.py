from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
    assert solution.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2) == [1, 2]

    print(solution.topKFrequent(nums=[1], k=1))
    assert solution.topKFrequent(nums=[1], k=1) == [1]

    print(solution.topKFrequent(nums=[-1, -1], k=1))
    assert solution.topKFrequent(nums=[-1, -1], k=1) == [-1]

    print(solution.topKFrequent(nums=[4, 1, -1, 2, -1, 2, 3], k=2))
    assert solution.topKFrequent(nums=[4, 1, -1, 2, -1, 2, 3], k=2) == [2, -1]
