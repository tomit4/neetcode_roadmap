import heapq
from collections import Counter, deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task 1 unit time
        # minimize idle time

        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = deque()  # paris of [-cnt, idleTime]

        while max_heap or queue:
            time += 1

            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    queue.append([cnt, time + n])

            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])

        return time


if __name__ == "__main__":
    solution = Solution()
    print(solution.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2))
    assert solution.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2) == 8
    print(solution.leastInterval(tasks=["A", "C", "A", "B", "D", "B"], n=1))
    assert solution.leastInterval(tasks=["A", "C", "A", "B", "D", "B"], n=1) == 6
    print(solution.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=3))
    assert solution.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=3) == 10
