from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0  # n ^ 0 = n
        for n in nums:
            res = n ^ res
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNumber(nums=[2, 2, 1]))
    assert solution.singleNumber(nums=[2, 2, 1]) == 1

    print(solution.singleNumber(nums=[4, 1, 2, 1, 2]))
    assert solution.singleNumber(nums=[4, 1, 2, 1, 2]) == 4

    print(solution.singleNumber(nums=[1]))
    assert solution.singleNumber(nums=[1]) == 1
