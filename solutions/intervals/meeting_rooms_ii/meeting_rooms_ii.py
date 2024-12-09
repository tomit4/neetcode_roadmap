from typing import List, Tuple


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def tuples_to_intervals(intervals: List[Tuple]) -> List[Interval]:
    return [Interval(start, end) for start, end in intervals]


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        start_pos, end_pos = 0, 0

        while start_pos < len(intervals):
            if start[start_pos] < end[end_pos]:
                start_pos += 1
                count += 1
            else:
                end_pos += 1
                count -= 1
            res = max(res, count)

        return res


if __name__ == "__main__":
    solution = Solution()
    intervals_1 = tuples_to_intervals(intervals=[(0, 40), (5, 10), (15, 20)])
    print(solution.minMeetingRooms(intervals=intervals_1))
    assert solution.minMeetingRooms(intervals=intervals_1) == 2

    intervals_2 = tuples_to_intervals(intervals=[(4, 9)])
    print(solution.minMeetingRooms(intervals=intervals_2))
    assert solution.minMeetingRooms(intervals=intervals_2) == 1
