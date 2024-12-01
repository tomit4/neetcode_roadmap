# 239. Sliding Window Maximum

[Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=DfljaUwZsOk&pp=ygUfbmVldGNvZGUgc2xpZGluZyB3aW5kb3cgbWF4aW11bQ%3D%3D)

You are given an array of integers `nums`, there is a sliding window of size `k`
which is moving from the very left of the array to the very right. You can only
see the `k` numbers in the window. Each time the sliding window moves right by
one position.

Return <em>the max sliding window</em>.

**Example 1:**

```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                        Max
---------------                       -----
[1  3  -1]  -3   5   3  6  7            3
 1 [3  -1   -3]  5   3  6  7            3
 1  3 [-1   -3   5]  3  6  7            5
 1  3  -1  [-3   5   3] 6  7            5
 1  3  -1   -3  [5   3  6] 7            6
 1  3  -1   -3   5  [3  6  7]           7
```

**Example 2:**

```
Input: nums = [1], k = 1
Output: [1]
```

**Constraints:**

- `1 <= nums.length <= 105`
- `-104 <= nums[i] <= 104`
- `1 <= k <= nums.length`
