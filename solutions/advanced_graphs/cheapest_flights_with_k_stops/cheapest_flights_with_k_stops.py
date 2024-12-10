from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights:  # s=source, d=destination, p=price
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p

            prices = tmpPrices

        return -1 if prices[dst] == float("inf") else int(prices[dst])


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
