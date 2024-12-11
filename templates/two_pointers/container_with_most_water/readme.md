# 11. Container With Most Water

[Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

[Neetcode Solution](https://www.youtube.com/watch?v=UuiTKBwPgAo&pp=ygUibmVldGNvZGUgY29udGFpbmVyIHdpdGggbW9zdCB3YXRlcg%3D%3D)

You are given an integer array `height` of length `n`. There are `n` vertical
lines drawn such that the two endpoints of the `i`<sup>th</sup> line are
`(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the <em>maximum amount of water a container can store</em>.

<b>Notice</b> that you may not slant the container.

**Example 1:**

<img src="./container_with_most_water.jpg" />

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.
```

**Example 2:**

```
Input: height = [1,1]
Output: 1
```

**Constraints:**

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`
