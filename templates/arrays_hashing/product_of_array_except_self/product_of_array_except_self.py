from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf(nums=[1, 2, 3, 4]))
    assert solution.productExceptSelf(nums=[1, 2, 3, 4]) == [24, 12, 8, 6]

    print(solution.productExceptSelf(nums=[-1, 1, 0, -3, 3]))
    assert solution.productExceptSelf(nums=[-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
