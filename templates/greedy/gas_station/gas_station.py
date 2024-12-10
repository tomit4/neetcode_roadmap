from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
    assert solution.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]) == 3

    print(solution.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
    assert solution.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]) == -1
