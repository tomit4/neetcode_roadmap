from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.partitionLabels(s="ababcbacadefegdehijhklij"))
    assert solution.partitionLabels(s="ababcbacadefegdehijhklij") == [9, 7, 8]

    print(solution.partitionLabels(s="eccbbbbdec"))
    assert solution.partitionLabels(s="eccbbbbdec") == [10]
