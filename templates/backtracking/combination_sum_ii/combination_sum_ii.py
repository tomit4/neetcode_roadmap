from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
    assert sorted(
        solution.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8)
    ) == sorted([[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
    print(solution.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))
    assert sorted(
        solution.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5)
    ) == sorted([[1, 2, 2], [5]])
