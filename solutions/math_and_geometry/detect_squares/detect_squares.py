from collections import defaultdict
from typing import List


class DetectSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for x, y in self.pts:
            if abs(py - y) != abs(px - x) or x == px or y == py:
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]

        return res


if __name__ == "__main__":
    detectSquares = DetectSquares()
    detectSquares.add(point=[3, 10])
    detectSquares.add(point=[11, 2])
    detectSquares.add(point=[3, 2])
    count_1 = detectSquares.count(point=[11, 10])
    print(count_1)
    assert count_1 == 1
    count_2 = detectSquares.count(point=[14, 8])
    print(count_2)
    assert count_2 == 0
    detectSquares.add(point=[11, 2])
    count_3 = detectSquares.count(point=[11, 10])
    print(count_3)
    assert count_3 == 2
