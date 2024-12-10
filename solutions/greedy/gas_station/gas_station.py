from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                start = i + 1

        return start


if __name__ == "__main__":
    solution = Solution()
    print(solution.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
    assert solution.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]) == 3

    print(solution.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
    assert solution.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]) == -1
