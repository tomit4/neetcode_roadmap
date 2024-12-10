from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}  # char -> last index in s

        # populate lastIndex map with last index of every character
        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.partitionLabels(s="ababcbacadefegdehijhklij"))
    assert solution.partitionLabels(s="ababcbacadefegdehijhklij") == [9, 7, 8]

    print(solution.partitionLabels(s="eccbbbbdec"))
    assert solution.partitionLabels(s="eccbbbbdec") == [10]
