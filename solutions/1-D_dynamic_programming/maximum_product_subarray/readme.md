# 152. Maximum Product Subarray

[Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=lXVy6YWFcRM&pp=ygUhbmVldGNvZGUgTWF4aW11bSBQcm9kdWN0IFN1YmFycmF5)

Given an integer array `nums`, find a subarray(a <b>subarray</b> is a contiguous
<b>non-empty</b> sequence of elements within an array) that has the largest
product, and return <em>the product.</em>

The test cases are generated so that the answer will fit in a <b>32-bit</b>
integer.

**Example 1:**

```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

**Example 2:**

```
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

**Constraints:**

- `1 <= nums.length <= 2 * 104`
- `-10 <= nums[i] <= 10`
- The product of any subarray of `nums` is <b>guaranteed</b> to fit in a
  <b>32-bit</b> integer.
