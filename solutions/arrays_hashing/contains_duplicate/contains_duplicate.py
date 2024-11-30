from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()

        for n in nums:
            if n in hash_set:
                return True
            hash_set.add(n)
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.hasDuplicate(nums=[1, 2, 3, 1]))
    print(solution.hasDuplicate(nums=[1, 2, 3, 4]))
    print(solution.hasDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
