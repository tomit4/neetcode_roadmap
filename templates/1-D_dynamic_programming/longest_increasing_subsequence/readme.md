# 300. Longest Increasing Subsequence

[Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=cjWnW0hdF1Y&pp=ygUnbmVldGNvZGUgTG9uZ2VzdCBJbmNyZWFzaW5nIFN1YnNlcXVlbmNl)

Given an integer array `nums`, return <em>the length of the longest <b>strictly
increasing subsequence (a subsequence is an array that can be derived from
another array by deleting some or no elements without changing the order of the
remaining elements).</b></em>

**Example 1:**

```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

**Example 2:**

```
Input: nums = [0,1,0,3,2,3]
Output: 4
```

**Example 3:**

```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

**Constraints:**

- `1 <= nums.length <= 2500`
- `-104 <= nums[i] <= 104`
