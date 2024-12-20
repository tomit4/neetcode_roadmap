from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}  # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[n] = i
        return [-1, -1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum(nums=[2, 7, 11, 15], target=9))
    print(solution.twoSum(nums=[3, 2, 4], target=6))
    print(solution.twoSum(nums=[3, 3], target=6))
