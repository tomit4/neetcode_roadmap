from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        return True


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
