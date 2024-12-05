from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.subsetsWithDup(nums=[1, 2, 2]))
    assert sorted(solution.subsetsWithDup(nums=[1, 2, 2])) == sorted(
        [
            [],
            [1],
            [1, 2],
            [1, 2, 2],
            [2],
            [2, 2],
        ]
    )
    print(solution.subsetsWithDup(nums=[0]))
    assert sorted(solution.subsetsWithDup(nums=[0])) == sorted([[], [0]])
