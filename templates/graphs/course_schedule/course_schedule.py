from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.canFinish(numCourses=2, prerequisites=[[1, 0]]))
    assert solution.canFinish(numCourses=2, prerequisites=[[1, 0]]) == True

    print(solution.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))
    assert solution.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]) == False
