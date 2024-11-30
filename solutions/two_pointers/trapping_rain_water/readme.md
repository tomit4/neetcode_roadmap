# 42. Trapping Rain Water

[Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=ZI2z5pq0TqA&pp=ygUcbmVldGNvZGUgdHJhcHBpbmcgcmFpbiB3YXRlcg%3D%3D)

Given `n` non-negative integers representing an elevation map where the width of
each bar is `1`, compute how much water it can trap after raining.

**Example 1:**

<img src="./trapping_rain_water.png" />

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by
array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water
(blue section) are being trapped.
```

**Example 2:**

```
Input: height = [4,2,0,3,2,5]
Output: 9
```

**Constraints:**

- `n == height.length`
- `1 <= n <= 2 * 104`
- `0 <= height[i] <= 105`
