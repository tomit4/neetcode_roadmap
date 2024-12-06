from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.findOrder(numCourses=2, prerequisites=[[1, 0]]))
    assert solution.findOrder(numCourses=2, prerequisites=[[1, 0]]) == [0, 1]

    print(
        sorted(
            solution.findOrder(
                numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]
            )
        )
    )
    assert sorted(
        solution.findOrder(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]])
    ) == sorted([0, 2, 1, 3])

    print(sorted(solution.findOrder(numCourses=1, prerequisites=[])))
    assert sorted(solution.findOrder(numCourses=1, prerequisites=[])) == sorted([0])
