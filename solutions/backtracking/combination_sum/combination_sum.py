from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def depth_first_search(i: int, cur: List[int], total: int):
            if total == target:
                res.append(cur.copy())  # don't pass cur itself
                return

            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            # left side of tree traversal
            depth_first_search(i, cur, total + candidates[i])

            cur.pop()
            # right side of tree traversal
            depth_first_search(i + 1, cur, total)

        depth_first_search(0, [], 0)

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum(candidates=[2, 3, 6, 7], target=7))
    assert sorted(solution.combinationSum(candidates=[2, 3, 6, 7], target=7)) == sorted(
        [[2, 2, 3], [7]]
    )
    print(solution.combinationSum(candidates=[2, 3, 5], target=8))
    assert sorted(solution.combinationSum(candidates=[2, 3, 5], target=8)) == sorted(
        [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    )
    print(solution.combinationSum(candidates=[2], target=1))
    assert sorted(solution.combinationSum(candidates=[2], target=1)) == sorted([])
