from typing import List


# establish res array of len nums populated by 1s...
# establish a prefix/postfix vars with value 1
# iterate through nums range assigning res[i]
# assign res[i] prefix
# assign prefix the current nums multiplied by itself
# iterate backwards through nums range
# assign res[i] postfix
# assign postfix the current nums multiplied by itself
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf(nums=[1, 2, 3, 4]))
    assert solution.productExceptSelf(nums=[1, 2, 3, 4]) == [24, 12, 8, 6]

    print(solution.productExceptSelf(nums=[-1, 1, 0, -3, 3]))
    assert solution.productExceptSelf(nums=[-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
