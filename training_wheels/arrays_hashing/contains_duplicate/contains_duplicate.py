from typing import List


# NOTE: NOT SOLVED
# create a set
# iterate through the nums array
# if the number is in the set
# return True
# otherwise add the number to the set
# return False after loop
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.containsDuplicate(nums=[1, 2, 3, 1]))
    assert solution.containsDuplicate(nums=[1, 2, 3, 1]) == True
    print(solution.containsDuplicate(nums=[1, 2, 3, 4]))
    assert solution.containsDuplicate(nums=[1, 2, 3, 4]) == False
    print(solution.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
    assert solution.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
