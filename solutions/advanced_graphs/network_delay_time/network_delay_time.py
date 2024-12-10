import heapq
from collections import defaultdict
from typing import List, Set


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Djikstra's Algorithm
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit: Set = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)

            # Breath First Search
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        return t if len(visit) == n else -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
    assert (
        solution.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2)
        == 2
    )

    print(solution.networkDelayTime(times=[[1, 2, 1]], n=2, k=1))
    assert solution.networkDelayTime(times=[[1, 2, 1]], n=2, k=1) == 1

    print(solution.networkDelayTime(times=[[1, 2, 1]], n=2, k=2))
    assert solution.networkDelayTime(times=[[1, 2, 1]], n=2, k=2) == -1
