from typing import List


# Establish a dictionary, map
# loop over the nums (enumerate, need index and value)
# grab the difference of the target and the current num
# if that difference exists within the dictionary, map
# return an array with the value of the map at the difference index, and the current index
# otherwise assign the map at number the current index
# after the loop return a two element array with -1 in each slot
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum(nums=[2, 7, 11, 15], target=9))
    assert solution.twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]

    print(solution.twoSum(nums=[3, 2, 4], target=6))
    assert solution.twoSum(nums=[3, 2, 4], target=6) == [1, 2]

    print(solution.twoSum(nums=[3, 3], target=6))
    assert solution.twoSum(nums=[3, 3], target=6) == [0, 1]
