from typing import List


# convert the nums array to a set
# establish a variable called longest and set it to 0
# iterate through the nums array
# if the num - 1 doesn't yet exist in the set
# establish a variable called length with an initial value of 0
# while the number plus the length is inside of the numSet
# continue to add one to the length
# reassign longest to the max value between length and longest
# return longest
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
    assert solution.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]) == 4

    print(solution.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    assert solution.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
