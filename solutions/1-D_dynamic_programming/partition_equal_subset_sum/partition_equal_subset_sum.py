from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()

            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP

        return True if target in dp else False


if __name__ == "__main__":
    solution = Solution()
    print(solution.canPartition(nums=[1, 5, 11, 5]))
    assert solution.canPartition(nums=[1, 5, 11, 5]) == True

    print(solution.canPartition(nums=[1, 2, 3, 5]))
    assert solution.canPartition(nums=[1, 2, 3, 5]) == False
