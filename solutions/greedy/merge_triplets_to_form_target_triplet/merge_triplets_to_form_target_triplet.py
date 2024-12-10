from typing import List, Set


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good: Set = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)

        return len(good) == 3


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.mergeTriplets(
            triplets=[[2, 5, 3], [1, 8, 4], [1, 7, 5]], target=[2, 7, 5]
        )
    )
    assert (
        solution.mergeTriplets(
            triplets=[[2, 5, 3], [1, 8, 4], [1, 7, 5]], target=[2, 7, 5]
        )
        == True
    )

    print(solution.mergeTriplets(triplets=[[3, 4, 5], [4, 5, 6]], target=[3, 2, 5]))
    assert (
        solution.mergeTriplets(triplets=[[3, 4, 5], [4, 5, 6]], target=[3, 2, 5])
        == False
    )

    print(
        solution.mergeTriplets(
            triplets=[[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], target=[5, 5, 5]
        )
    )
    assert (
        solution.mergeTriplets(
            triplets=[[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], target=[5, 5, 5]
        )
        == True
    )
