from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adjacency list of prerequisites
        prerequisites_map = {course: [] for course in range(numCourses)}

        for course, prerequisite in prerequisites:
            prerequisites_map[course].append(prerequisite)

        # a course has 3 possible states:
        # visited -> course has been added to output
        # visiting -> course not added to output, but added to cycle
        # unvisited -> course not added to output or cycle

        output = []
        visit = set()
        cycle = set()

        def depth_first_search(course):
            if course in cycle:
                return False
            if course in visit:
                return True

            cycle.add(course)
            for prerequisite in prerequisites_map[course]:
                if depth_first_search(prerequisite) == False:
                    return False

            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True

        for course in range(numCourses):
            if depth_first_search(course) == False:
                return []

        return output


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
