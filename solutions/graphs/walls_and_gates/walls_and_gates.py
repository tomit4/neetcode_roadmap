from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> List[List[int]]:
        ROWS = len(rooms)
        COLS = len(rooms[0])
        visited = set()

        queue = deque()

        def addRoom(row, col):
            if (
                row < 0
                or row == ROWS
                or col < 0
                or col == COLS
                or (row, col) in visited
                or rooms[row][col] == -1
            ):
                return
            visited.add((row, col))
            queue.append([row, col])

        for row in range(ROWS):
            for col in range(COLS):
                if rooms[row][col] == 0:  # is a gate
                    queue.append([row, col])
                    visited.add((row, col))

        dist = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                rooms[row][col] = dist

                addRoom(row + 1, col)
                addRoom(row - 1, col)
                addRoom(row, col + 1)
                addRoom(row, col - 1)

            dist += 1

        return rooms


if __name__ == "__main__":
    solution = Solution()
    input_rooms = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647],
    ]
    expected_output = [
        [3, -1, 0, 1],
        [2, 2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, 4],
    ]
    output = solution.wallsAndGates(
        rooms=[row[:] for row in input_rooms]
    )  # Deep copy for testing
    print("Output:", output)
    print("Expected:", expected_output)
    assert output == expected_output, "Test case 1 failed!"

    input_rooms = [[0, -1], [2147483647, 2147483647]]
    expected_output = [[0, -1], [1, 2]]
    output = solution.wallsAndGates(
        rooms=[row[:] for row in input_rooms]
    )  # Deep copy for testing
    print("Output:", output)
    print("Expected:", expected_output)
    assert output == expected_output, "Test case 2 failed!"
