from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> List[List[int]]:
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
