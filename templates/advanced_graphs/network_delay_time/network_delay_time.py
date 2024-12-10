from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        return 0


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
