from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left: int = 0
        right: int = len(numbers) - 1

        while left < right:
            cur_sum: int = numbers[left] + numbers[right]
            if cur_sum > target:
                right -= 1
            elif cur_sum < target:
                left += 1
            else:
                return [left + 1, right + 1]

        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum(numbers=[2, 7, 11, 15], target=9))
    print(solution.twoSum(numbers=[2, 3, 4], target=6))
    print(solution.twoSum(numbers=[-1, 0], target=-1))
