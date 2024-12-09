# 57. Insert Interval

[Insert Interval](https://leetcode.com/problems/insert-interval/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=A8NUOmlwOlM&pp=ygUYbmVldGNvZGUgSW5zZXJ0IEludGVydmFs)

You are given an array of non-overlapping intervals `intervals` where
`intervals[i]
= [start`<sub>i</sub>`, end`<sub>i</sub>`]` represent the start
and the end of the `i`<sup>th</sup> interval and `intervals` is sorted in
ascending order by `start`<sub>i</sub>. You are also given an interval
`newInterval = [start, end]` that represents the start and end of another
interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in
ascending order by `start`<sub>i</sub> and `intervals` still does not have any
overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` <em>after the insertion.</em>

<b>Note</b> that you don't need to modify `intervals` in-place. You can make a
new array and return it.

**Example 1:**

```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

**Example 2:**

```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

**Constraints:**

- `0 <= intervals.length <= 104`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 105`
- `intervals` is sorted by `start`<sub>i</sub> in <b>ascending</b> order.
- `newInterval.length == 2`
- `0 <= start <= end <= 10^5`
