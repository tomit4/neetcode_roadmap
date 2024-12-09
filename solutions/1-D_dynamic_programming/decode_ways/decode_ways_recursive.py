class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def depth_first_search(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = depth_first_search(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                res += depth_first_search(i + 2)
            dp[i] = res
            return res

        return depth_first_search(0)


if __name__ == "__main__":
    solution = Solution()
    print(solution.numDecodings(s="12"))
    assert solution.numDecodings(s="12") == 2

    print(solution.numDecodings(s="226"))
    assert solution.numDecodings(s="226") == 3

    print(solution.numDecodings(s="06"))
    assert solution.numDecodings(s="06") == 0
