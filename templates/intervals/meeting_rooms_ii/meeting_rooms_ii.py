from typing import List, Tuple


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def tuples_to_intervals(intervals: List[Tuple]) -> List[Interval]:
    return [Interval(start, end) for start, end in intervals]


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    intervals_1 = tuples_to_intervals(intervals=[(0, 40), (5, 10), (15, 20)])
    print(solution.minMeetingRooms(intervals=intervals_1))
    assert solution.minMeetingRooms(intervals=intervals_1) == 2

    intervals_2 = tuples_to_intervals(intervals=[(4, 9)])
    print(solution.minMeetingRooms(intervals=intervals_2))
    assert solution.minMeetingRooms(intervals=intervals_2) == 1
