from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.swimInWater(grid=[[0, 2], [1, 3]]))
    assert solution.swimInWater(grid=[[0, 2], [1, 3]]) == 3

    print(
        solution.swimInWater(
            grid=[
                [0, 1, 2, 3, 4],
                [24, 23, 22, 21, 5],
                [12, 13, 14, 15, 16],
                [11, 17, 18, 19, 20],
                [10, 9, 8, 7, 6],
            ]
        )
    )
    assert (
        solution.swimInWater(
            grid=[
                [0, 1, 2, 3, 4],
                [24, 23, 22, 21, 5],
                [12, 13, 14, 15, 16],
                [11, 17, 18, 19, 20],
                [10, 9, 8, 7, 6],
            ]
        )
        == 16
    )
