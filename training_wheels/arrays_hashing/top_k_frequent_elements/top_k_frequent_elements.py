from typing import List


# Establish a dict called count
# establish a matrix called freq which has empty arrays
# the amount of arrays in freq is the length of the nums array + 1 (use an inline for loop to populate)
# iterate over each key/value pair of the count using count.items and a for loop
# at each index of freq, append the count value (i.e. number) that appears at that index
# establish an empty res array
# iterate in reverse order of the frequency matrix
# create an inner for loop that iterates over the values of whatever exists at freq[i]
# continually append the number to res
# check if the len of res is equal to k
# if it is, then return the res
# return an empty array at the end (will never execute)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
    assert solution.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2) == [1, 2]

    print(solution.topKFrequent(nums=[1], k=1))
    assert solution.topKFrequent(nums=[1], k=1) == [1]

    print(solution.topKFrequent(nums=[-1, -1], k=1))
    assert solution.topKFrequent(nums=[-1, -1], k=1) == [-1]

    print(solution.topKFrequent(nums=[4, 1, -1, 2, -1, 2, 3], k=2))
    assert solution.topKFrequent(nums=[4, 1, -1, 2, -1, 2, 3], k=2) == [2, -1]
