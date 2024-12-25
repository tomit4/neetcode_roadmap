from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
    assert solution.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0) == 4

    print(solution.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
    assert solution.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3) == -1

    print(solution.search(nums=[1], target=0))
    assert solution.search(nums=[1], target=0) == -1

    print(solution.search(nums=[1, 3], target=3))
    assert solution.search(nums=[1, 3], target=3) == 1

    print(solution.search(nums=[3, 5, 1], target=3))
    assert solution.search(nums=[3, 5, 1], target=3) == 0
