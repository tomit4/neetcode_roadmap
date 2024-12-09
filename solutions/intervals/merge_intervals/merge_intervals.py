from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn)
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = output[-1][1]

            if start <= last_end:
                output[-1][1] = max(last_end, end)
            else:
                output.append([start, end])

        return output


if __name__ == "__main__":
    solution = Solution()
    print(solution.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
    assert solution.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6],
        [8, 10],
        [15, 18],
    ]

    print(solution.merge(intervals=[[1, 4], [4, 5]]))
    assert solution.merge(intervals=[[1, 4], [4, 5]]) == [[1, 5]]
