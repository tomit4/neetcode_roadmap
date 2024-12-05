from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res: List[List[str]] = []
        part: List[str] = []

        def depth_first_search(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j):
                    part.append(s[i : j + 1])
                    depth_first_search(j + 1)
                    part.pop()

        depth_first_search(0)

        return res

    def is_palindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.partition(s="aab"))
    assert solution.partition(s="aab") == [["a", "a", "b"], ["aa", "b"]]
    print(solution.partition(s="a"))
    assert solution.partition(s="a") == [["a"]]
