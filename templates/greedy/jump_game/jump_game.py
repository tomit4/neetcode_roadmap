from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.canJump(nums=[2, 3, 1, 1, 4]))
    assert solution.canJump(nums=[2, 3, 1, 1, 4]) == True

    print(solution.canJump(nums=[3, 2, 1, 0, 4]))
    assert solution.canJump(nums=[3, 2, 1, 0, 4]) == False
