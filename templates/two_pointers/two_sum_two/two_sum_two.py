from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum(numbers=[2, 7, 11, 15], target=9))
    assert solution.twoSum(numbers=[2, 7, 11, 15], target=9) == [1, 2]

    print(solution.twoSum(numbers=[2, 3, 4], target=6))
    assert solution.twoSum(numbers=[2, 3, 4], target=6) == [1, 3]

    print(solution.twoSum(numbers=[-1, 0], target=-1))
    assert solution.twoSum(numbers=[-1, 0], target=-1) == [1, 2]
