class MedianFinder:

    def __init__(self):
        return

    def addNum(self, num: int) -> None:
        return

    def findMedian(self) -> float:
        return 0.0


if __name__ == "__main__":
    median_finder = MedianFinder()
    median_finder.addNum(1)
    median_finder.addNum(2)
    print(median_finder.findMedian())
    assert median_finder.findMedian() == 1.5
    median_finder.addNum(3)
    print(median_finder.findMedian())
    assert median_finder.findMedian() == 2.0
