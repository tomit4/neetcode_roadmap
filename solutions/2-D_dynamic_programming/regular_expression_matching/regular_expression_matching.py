class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # TOP-Down Memoization

        def depth_first_search(i, j) -> bool:
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < len(p) and p[j + 1] == "*":
                return depth_first_search(i, j + 2) or (  # don't use the *
                    match and depth_first_search(i + 1, j)  # use the *
                )

            if match:
                return depth_first_search(i + 1, j + 1)

            return False

        return depth_first_search(0, 0)


if __name__ == "__main__":
    solution = Solution()
    print(solution.isMatch(s="aa", p="a"))
    assert solution.isMatch(s="aa", p="a") == False

    print(solution.isMatch(s="aa", p="a*"))
    assert solution.isMatch(s="aa", p="a*") == True

    print(solution.isMatch(s="ab", p=".*"))
    assert solution.isMatch(s="ab", p=".*") == True
