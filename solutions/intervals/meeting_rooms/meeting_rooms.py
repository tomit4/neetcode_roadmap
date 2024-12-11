from typing import List, Tuple


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def tuples_to_intervals(intervals: List[Tuple]) -> List[Interval]:
    return [Interval(start, end) for start, end in intervals]


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            i_1 = intervals[i - 1]
            i_2 = intervals[i]

            if i_1.end > i_2.start:
                return False

        return True


if __name__ == "__main__":
    solution = Solution()
    intervals_1 = tuples_to_intervals(intervals=[(0, 30), (5, 10), (15, 20)])
    print(solution.canAttendMeetings(intervals=intervals_1))
    assert solution.canAttendMeetings(intervals=intervals_1) == False

    intervals_2 = tuples_to_intervals(intervals=[(5, 8), (9, 15)])
    print(solution.canAttendMeetings(intervals=intervals_2))
    assert solution.canAttendMeetings(intervals=intervals_2) == True