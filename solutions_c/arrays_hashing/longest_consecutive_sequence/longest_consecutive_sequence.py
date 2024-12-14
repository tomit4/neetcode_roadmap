from typing import List, Set


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set: Set[int] = set(nums)
        longest: int = 0

        for n in nums:
            # check if its the start 9f a sequence
            if (n - 1) not in num_set:
                length: int = 0
                while (n + length) in num_set:
                    length += 1
                longest = max(length, longest)

        return longest


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
    print(solution.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
