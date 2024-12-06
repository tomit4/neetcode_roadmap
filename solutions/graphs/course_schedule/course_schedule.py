from re import A
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to a prerequisites list
        prerequisuites_map = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            prerequisuites_map[course].append(pre)

        # visited_set = all courses along the curr DFS path
        visited_set = set()

        def depth_first_search(course):
            if course in visited_set:
                return False
            if prerequisuites_map[course] == []:
                return True

            visited_set.add(course)
            for prerequisite in prerequisuites_map[course]:
                if not depth_first_search(prerequisite):
                    return False

            visited_set.remove(course)
            prerequisuites_map[course] = []

            return True

        for course in range(numCourses):
            if not depth_first_search(course):
                return False

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.canFinish(numCourses=2, prerequisites=[[1, 0]]))
    assert solution.canFinish(numCourses=2, prerequisites=[[1, 0]]) == True

    print(solution.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))
    assert solution.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]) == False
