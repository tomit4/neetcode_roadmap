from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return [0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum(nums=[2, 7, 11, 15], target=9))
    assert solution.twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]

    print(solution.twoSum(nums=[3, 2, 4], target=6))
    assert solution.twoSum(nums=[3, 2, 4], target=6) == [1, 2]

    print(solution.twoSum(nums=[3, 3], target=6))
    assert solution.twoSum(nums=[3, 3], target=6) == [0, 1]
