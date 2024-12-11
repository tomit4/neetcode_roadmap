from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return 0.0


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
    assert solution.findMedianSortedArrays(nums1=[1, 3], nums2=[2]) == 2.00000

    print(solution.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))
    assert solution.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]) == 2.50000
