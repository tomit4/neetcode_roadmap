from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        return []


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.pacificAtlantic(
            heights=[
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4],
            ]
        )
    )
    assert solution.pacificAtlantic(
        heights=[
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
    ) == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]

    print(solution.pacificAtlantic(heights=[[1]]))
    assert solution.pacificAtlantic(heights=[[1]]) == [[0, 0]]
