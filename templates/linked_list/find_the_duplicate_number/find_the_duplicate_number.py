from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    solution_1 = solution.findDuplicate(nums=[1, 3, 4, 2, 2])
    print(solution_1)
    solution_2 = solution.findDuplicate(nums=[3, 1, 3, 4, 2])
    print(solution_2)
    solution_3 = solution.findDuplicate(nums=[3, 3, 3, 3, 3])
    print(solution_3)
