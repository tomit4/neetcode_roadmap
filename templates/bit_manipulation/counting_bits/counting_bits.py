from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.countBits(n=2))
    assert solution.countBits(n=2) == [0, 1, 1]

    print(solution.countBits(n=5))
    assert solution.countBits(n=5) == [0, 1, 1, 2, 1, 2]
