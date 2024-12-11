# 287. Find the Duplicate Number

[Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=wjYnzkAhcNk&pp=ygUibmVldGNvZGUgZmluZCB0aGUgZHVwbGljYXRlIG51bWJlcg%3D%3D)

Given an array of integers `nums` containing `n + 1` integers where each integer
is in the range `[1, n]` inclusive.

There is only <b>one repeated number</b> in `nums`, return <em>this repeated
number.</em>

You must solve the problem <b>without</b> modifying the array `nums` and using
only constant extra space.

**Example 1:**

```
Input: nums = [1,3,4,2,2]
Output: 2
```

**Example 2:**

```
Input: nums = [3,1,3,4,2]
Output: 3
```

**Example 3:**

```
Input: nums = [3,3,3,3,3]
Output: 3
```

**Constraints:**

- `1 <= n <= 10^5`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`
- All the integers in `nums` appear only <b>once</b> except for <b>precisely one
  integer</b> which appears <b>two or more</b> times.
