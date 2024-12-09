from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.rob(nums=[2, 3, 2]))
    assert solution.rob(nums=[2, 3, 2]) == 3

    print(solution.rob(nums=[1, 2, 3, 1]))
    assert solution.rob(nums=[1, 2, 3, 1]) == 4

    print(solution.rob(nums=[1, 2, 3]))
    assert solution.rob(nums=[1, 2, 3]) == 3
