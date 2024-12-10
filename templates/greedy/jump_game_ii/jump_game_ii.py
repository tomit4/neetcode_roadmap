from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.jump(nums=[2, 3, 1, 1, 4]))
    assert solution.jump(nums=[2, 3, 1, 1, 4]) == 2

    print(solution.jump(nums=[2, 3, 0, 1, 4]))
    assert solution.jump(nums=[2, 3, 0, 1, 4]) == 2
