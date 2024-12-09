# 56. Merge Intervals

[Merge Intervals](https://leetcode.com/problems/merge-intervals/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=44H3cEC2fFM&pp=ygUYbmVldGNvZGUgTWVyZ2UgSW50ZXJ2YWxz)

Given an array of `intervals` where
`intervals[i] = [start`<sub>i</sub>`, end`<sub>i</sub>`]`, merge all overlapping
intervals, and return <em>an array of the non-overlapping intervals that cover
all the intervals in the input.</em>

**Example 1:**

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
```

**Example 2:**

```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

**Constraints:**

- `1 <= intervals.length <= 104`
- `intervals[i].length == 2`
- `0 <= start`<sub>i</sub>`<= end`<sub>i</sub>`<= 104`
