from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2))
    assert solution.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2) == 8
    print(solution.leastInterval(tasks=["A", "C", "A", "B", "D", "B"], n=1))
    assert solution.leastInterval(tasks=["A", "C", "A", "B", "D", "B"], n=1) == 6
    print(solution.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=3))
    assert solution.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=3) == 10
