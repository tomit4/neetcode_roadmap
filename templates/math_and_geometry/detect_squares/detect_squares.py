from typing import List


class DetectSquares:

    def __init__(self):
        return

    def add(self, point: List[int]) -> None:
        return

    def count(self, point: List[int]) -> int:
        return 0


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
