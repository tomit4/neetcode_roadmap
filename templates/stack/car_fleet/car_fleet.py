from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3])
    )
    print(solution.carFleet(target=10, position=[3], speed=[3]))
    print(solution.carFleet(target=100, position=[0, 2, 4], speed=[4, 2, 1]))
