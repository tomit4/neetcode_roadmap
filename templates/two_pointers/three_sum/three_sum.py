from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
    assert solution.threeSum(nums=[-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]

    print(solution.threeSum(nums=[0, 1, 1]))
    assert solution.threeSum(nums=[0, 1, 1]) == []

    print(solution.threeSum(nums=[0, 0, 0]))
    assert solution.threeSum(nums=[0, 0, 0]) == [[0, 0, 0]]
