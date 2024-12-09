from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.canPartition(nums=[1, 5, 11, 5]))
    assert solution.canPartition(nums=[1, 5, 11, 5]) == True

    print(solution.canPartition(nums=[1, 2, 3, 5]))
    assert solution.canPartition(nums=[1, 2, 3, 5]) == False
