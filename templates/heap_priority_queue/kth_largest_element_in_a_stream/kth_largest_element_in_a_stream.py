from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minHeap with K largest integers
        return

    def add(self, val: int) -> int:
        return 0


if __name__ == "__main__":
    kth_largest = KthLargest(k=3, nums=[4, 5, 8, 2])
    assert kth_largest.add(3) == 4
    assert kth_largest.add(5) == 5
    assert kth_largest.add(10) == 5
    assert kth_largest.add(9) == 8
    assert kth_largest.add(4) == 8
    print("first test case passed!!")

    kth_largest_2 = KthLargest(k=4, nums=[7, 7, 7, 7, 8, 3])
    assert kth_largest_2.add(2) == 7
    assert kth_largest_2.add(10) == 7
    assert kth_largest_2.add(9) == 7
    assert kth_largest_2.add(9) == 8
    print("second test case passed!!")