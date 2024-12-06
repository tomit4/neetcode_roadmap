from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adjacency_list = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adjacency_list[n1].append(n2)
            adjacency_list[n2].append(n1)

        visited = set()

        def depth_first_search(i, prev):
            if i in visited:
                return False

            visited.add(i)
            # check the neighbors of i
            for j in adjacency_list[i]:
                if j == prev:
                    continue
                if not depth_first_search(j, i):
                    return False
            return True

        return depth_first_search(0, -1) and n == len(visited)


if __name__ == "__main__":
    solution = Solution()
    print(solution.validTree(n=5, edges=[[0, 1], [0, 2], [0, 3], [1, 4]]))
    assert solution.validTree(n=5, edges=[[0, 1], [0, 2], [0, 3], [1, 4]]) == True

    print(solution.validTree(n=5, edges=[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
    assert (
        solution.validTree(n=5, edges=[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False
    )
