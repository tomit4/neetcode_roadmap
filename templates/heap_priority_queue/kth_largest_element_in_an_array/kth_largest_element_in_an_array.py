from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
    assert (solution.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2)) == 5
    print(solution.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
    assert (solution.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4)) == 4
