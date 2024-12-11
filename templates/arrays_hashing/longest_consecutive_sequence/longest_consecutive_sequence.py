from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
    assert solution.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]) == 4

    print(solution.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    assert solution.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
