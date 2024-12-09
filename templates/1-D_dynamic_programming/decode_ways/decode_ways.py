class Solution:
    def numDecodings(self, s: str) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.numDecodings(s="12"))
    assert solution.numDecodings(s="12") == 2

    print(solution.numDecodings(s="226"))
    assert solution.numDecodings(s="226") == 3

    print(solution.numDecodings(s="06"))
    assert solution.numDecodings(s="06") == 0
