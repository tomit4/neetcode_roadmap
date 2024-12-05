from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.subsets(nums=[1, 2, 3]))
    assert sorted(solution.subsets(nums=[1, 2, 3])) == sorted(
        [
            [],
            [1],
            [2],
            [1, 2],
            [3],
            [1, 3],
            [2, 3],
            [1, 2, 3],
        ]
    )
    print(solution.subsets(nums=[0]))
    assert sorted(solution.subsets(nums=[0])) == sorted([[], [0]])
