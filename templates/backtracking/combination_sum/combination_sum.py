from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return []


if __name__ == "main":
    solution = Solution()
    print(solution.combinationSum(candidates=[2, 3, 6, 7], target=7))
    assert sorted(solution.combinationSum(candidates=[2, 3, 6, 7], target=7)) == sorted(
        [[2, 2, 3], [7]]
    )
    print(solution.combinationSum(candidates=[2, 3, 5], target=8))
    assert sorted(solution.combinationSum(candidates=[2, 3, 5], target=8)) == sorted(
        [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    )
    print(solution.combinationSum(candidates=[2], target=1))
    assert sorted(solution.combinationSum(candidates=[2], target=1)) == sorted([])
