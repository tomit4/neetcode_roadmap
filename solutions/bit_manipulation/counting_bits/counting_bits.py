from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp


if __name__ == "__main__":
    solution = Solution()
    print(solution.countBits(n=2))
    assert solution.countBits(n=2) == [0, 1, 1]

    print(solution.countBits(n=5))
    assert solution.countBits(n=5) == [0, 1, 1, 2, 1, 2]
