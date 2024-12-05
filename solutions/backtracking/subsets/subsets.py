from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def depth_first_search(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i])
            depth_first_search(i + 1)

            # decision NOT to include nums[i]
            subset.pop()
            depth_first_search(i + 1)

        depth_first_search(0)

        return res


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
