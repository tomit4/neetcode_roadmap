class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def depth_first_search(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == t[j]:
                cache[(i, j)] = depth_first_search(i + 1, j + 1) + depth_first_search(
                    i + 1, j
                )
            else:
                cache[(i, j)] = depth_first_search(i + 1, j)
            return cache[(i, j)]

        return depth_first_search(0, 0)


if __name__ == "__main__":
    solution = Solution()
    print(solution.numDistinct(s="rabbbit", t="rabbit"))
    assert solution.numDistinct(s="rabbbit", t="rabbit") == 3

    print(solution.numDistinct(s="babgbag", t="bag"))
    assert solution.numDistinct(s="babgbag", t="bag") == 5
