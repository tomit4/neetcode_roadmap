from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A: List[int] = nums1
        B: List[int] = nums2
        total: int = len(nums1) + len(nums2)
        half: int = total // 2

        if len(B) < len(A):
            A, B = B, A

        left: int = 0
        right: int = len(A) - 1

        while True:
            i: int = (left + right) // 2  # A
            j: int = half - i - 2  # B

            A_left = A[i] if i >= 0 else float("-infinity")
            A_right = A[i + 1] if (i + 1) < len(A) else float("infinity")
            B_left = B[j] if j >= 0 else float("-infinity")
            B_right = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # left partition is correct
            if A_left <= B_right and B_left <= A_right:
                # odd number of elements
                if total % 2:
                    return min(A_right, B_right)
                # even number of elements
                else:
                    min_plus_max: float = max(A_left, B_left) + min(A_right, B_right)
                    return min_plus_max / 2
            elif A_left > B_right:
                right = i - 1
            else:
                left = i + 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
    print(solution.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))
