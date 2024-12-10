from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.findCheapestPrice(
            n=4,
            flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
            src=0,
            dst=3,
            k=1,
        )
    )
    assert (
        solution.findCheapestPrice(
            n=4,
            flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
            src=0,
            dst=3,
            k=1,
        )
        == 700
    )

    print(
        solution.findCheapestPrice(
            n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1
        )
    )
    assert (
        solution.findCheapestPrice(
            n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1
        )
        == 200
    )

    print(
        solution.findCheapestPrice(
            n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0
        )
    )
    assert (
        solution.findCheapestPrice(
            n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0
        )
        == 500
    )
