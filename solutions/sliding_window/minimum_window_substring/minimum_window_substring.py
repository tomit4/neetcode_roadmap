from typing import Dict, List


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count_t: Dict[str, int] = {}
        window: Dict[str, int] = {}

        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        have: int = 0
        need: int = len(count_t)
        res: List[int] = [-1, -1]
        res_len: float = float("infinity")

        left: int = 0
        for right in range(len(s)):
            c: str = s[right]
            window[c] = 1 + window.get(c, 0)

            if c in count_t and window[c] == count_t[c]:
                have += 1

            while have == need:
                # update our result
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                # pop from the left of our window
                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1
        left, right = res

        return s[left : right + 1] if res_len != float("infinity") else ""


if __name__ == "__main__":
    solution = Solution()
    print(solution.minWindow(s="ADOBECODEBANC", t="ABC"))
    print(solution.minWindow(s="a", t="a"))
    print(solution.minWindow(s="a", t="aa"))
