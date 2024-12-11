class Solution:
    def minWindow(self, s: str, t: str) -> str:
        return ""


if __name__ == "__main__":
    solution = Solution()
    print(solution.minWindow(s="ADOBECODEBANC", t="ABC"))
    assert solution.minWindow(s="ADOBECODEBANC", t="ABC") == "BANC"

    print(solution.minWindow(s="a", t="a"))
    assert solution.minWindow(s="a", t="a") == "a"

    print(solution.minWindow(s="a", t="aa"))
    assert solution.minWindow(s="a", t="aa") == ""
