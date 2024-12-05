from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.partition(s="aab"))
    assert solution.partition(s="aab") == [["a", "a", "b"], ["aa", "b"]]
    print(solution.partition(s="a"))
    assert solution.partition(s="a") == [["a"]]
