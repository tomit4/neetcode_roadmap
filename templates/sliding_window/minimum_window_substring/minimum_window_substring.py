class Solution:
    def minWindow(self, s: str, t: str) -> str:
        return ""


if __name__ == "__main__":
    solution = Solution()
    print(solution.minWindow(s="ADOBECODEBANC", t="ABC"))
    print(solution.minWindow(s="a", t="a"))
    print(solution.minWindow(s="a", t="aa"))
