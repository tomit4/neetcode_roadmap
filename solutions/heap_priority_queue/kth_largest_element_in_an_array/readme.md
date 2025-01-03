# 215. Kth Largest Element in an Array

[Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=XEmy13g1Qxc&pp=ygUobmVldGNvZGUgS3RoIExhcmdlc3QgRWxlbWVudCBJbiBBbiBBcnJheQ%3D%3D)

Given an integer array `nums` and an integer `k`, return the `k`<sup>th</sup>
<em>largest element in the array.</em>

Note that it is the `k`<sup>th</sup> largest element in the sorted order, not
the `k`<sup>th</sup> distinct element.

Can you solve it without sorting?

**Example 1:**

```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

**Example 2:**

```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

**Constraints:**

- `1 <= k <= nums.length <= 105`
- `-104 <= nums[i] <= 104`
