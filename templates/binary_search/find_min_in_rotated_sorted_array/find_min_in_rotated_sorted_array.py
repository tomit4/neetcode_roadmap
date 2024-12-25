from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMin(nums=[3, 4, 5, 1, 2]))
    assert solution.findMin(nums=[3, 4, 5, 1, 2]) == 1
    print(solution.findMin(nums=[4, 5, 6, 7, 0, 1, 2]))
    assert solution.findMin(nums=[4, 5, 6, 7, 0, 1, 2]) == 0
    print(solution.findMin(nums=[11, 13, 15, 17]))
    assert solution.findMin(nums=[11, 13, 15, 17]) == 11
