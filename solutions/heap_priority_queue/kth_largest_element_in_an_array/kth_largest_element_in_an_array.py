from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Quick Select Algorithm
        k = len(nums) - k

        def quick_select(left, right):
            pivot = nums[right]
            ptr = left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[ptr], nums[i] = nums[i], nums[ptr]  # swap without temp var
                    ptr += 1

            nums[ptr], nums[right] = nums[right], nums[ptr]

            if ptr > k:
                return quick_select(left, ptr - 1)
            elif ptr < k:
                return quick_select(ptr + 1, right)
            else:
                return nums[ptr]

        return quick_select(0, len(nums) - 1)


if __name__ == "__main__":
    solution = Solution()
    print(solution.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
    assert (solution.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2)) == 5
    print(solution.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
    assert (solution.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4)) == 4
