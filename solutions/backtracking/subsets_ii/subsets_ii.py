from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)

            subset.pop()
            # All subsets that don't include nums[i]
            # skip all duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            backtrack(i + 1, subset)

        backtrack(0, [])

        return res


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
