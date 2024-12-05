from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        # base case
        if len(nums) == 1:
            #  return [nums.copy()]
            return [nums[:]]

        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)

        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.permute(nums=[1, 2, 3]))
    assert sorted(solution.permute(nums=[1, 2, 3])) == sorted(
        [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ]
    )
    print(solution.permute(nums=[0, 1]))
    assert sorted(solution.permute(nums=[0, 1])) == sorted([[0, 1], [1, 0]])
    print(solution.permute(nums=[1]))
    assert sorted(solution.permute(nums=[1])) == sorted([[1]])
