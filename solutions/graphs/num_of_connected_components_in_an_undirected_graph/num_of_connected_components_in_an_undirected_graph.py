from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union Find Algorithm
        parents = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            while res != parents[res]:
                # path compression
                parents[res] = parents[parents[res]]
                res = parents[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            # did not find union
            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                parents[p1] = p2
                rank[p2] += rank[p1]
            else:
                parents[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.countComponents(n=3, edges=[[0, 1], [0, 2]]))
    assert solution.countComponents(n=3, edges=[[0, 1], [0, 2]]) == 1

    print(solution.countComponents(n=6, edges=[[0, 1], [1, 2], [2, 3], [4, 5]]))
    assert solution.countComponents(n=6, edges=[[0, 1], [1, 2], [2, 3], [4, 5]]) == 2

    print(solution.countComponents(n=5, edges=[[0, 1], [1, 2], [3, 4]]))
    assert solution.countComponents(n=5, edges=[[0, 1], [1, 2], [3, 4]]) == 2
