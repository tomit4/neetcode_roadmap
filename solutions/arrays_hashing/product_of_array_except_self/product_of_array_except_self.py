from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res: List[int] = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf(nums=[1, 2, 3, 4]))
    print(solution.productExceptSelf(nums=[-1, 1, 0, -3, 3]))
