# 84. Largest Rectangle in Histogram

[Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=zx5Sw9130L0)

Given an array of integers `heights` representing the histogram's bar height
where the width of each bar is `1`, return <em>the area of the largest rectangle
in the histogram.</em>

**Example 1:**

<img src="./largest_rectangle_in_histogram_01.jpg" />

```
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1. The largest
rectangle is shown in the red area, which has an area = 10 units.
```

**Example 2:**

<img src="./largest_rectangle_in_histogram_02.jpg" />

```
Input: heights = [2,4]
Output: 4
```

**Constraints:**

- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`
