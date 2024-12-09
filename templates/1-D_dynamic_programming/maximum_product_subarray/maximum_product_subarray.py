from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProduct(nums=[2, 3, -2, 4]))
    assert solution.maxProduct(nums=[2, 3, -2, 4]) == 6

    print(solution.maxProduct(nums=[-2, 0, -1]))
    assert solution.maxProduct(nums=[-2, 0, -1]) == 0
