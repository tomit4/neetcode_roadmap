import heapq

# NOTE: Ends up being a comparison between
# the root of a maxheap and the root of a minheap


class MedianFinder:

    def __init__(self):
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # make sure every num small is <= every num in large
        if self.small and self.large and ((-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # uneven size?
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return ((-1 * self.small[0]) + self.large[0]) / 2


if __name__ == "__main__":
    median_finder = MedianFinder()
    median_finder.addNum(1)
    median_finder.addNum(2)
    print(median_finder.findMedian())
    assert median_finder.findMedian() == 1.5
    median_finder.addNum(3)
    print(median_finder.findMedian())
    assert median_finder.findMedian() == 2.0
