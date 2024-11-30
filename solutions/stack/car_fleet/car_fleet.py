from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]  # list comprehension

        stack = []
        for p, s in sorted(pair)[::-1]:  # Reverse Sored Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3])
    )
    print(solution.carFleet(target=10, position=[3], speed=[3]))
    print(solution.carFleet(target=100, position=[0, 2, 4], speed=[4, 2, 1]))
