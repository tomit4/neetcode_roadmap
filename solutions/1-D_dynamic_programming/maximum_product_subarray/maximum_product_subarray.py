from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax, curMin)

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProduct(nums=[2, 3, -2, 4]))
    assert solution.maxProduct(nums=[2, 3, -2, 4]) == 6

    print(solution.maxProduct(nums=[-2, 0, -1]))
    assert solution.maxProduct(nums=[-2, 0, -1]) == 0
