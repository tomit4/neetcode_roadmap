from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        nums.sort()

        for i, a in enumerate(nums):
            # skip ahead if value is same as last value
            if i > 0 and a == nums[i - 1]:
                continue

            left: int = i + 1
            right: int = len(nums) - 1

            while left < right:
                three_sum: int = a + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
    print(solution.threeSum(nums=[0, 1, 1]))
    print(solution.threeSum(nums=[0, 0, 0]))
