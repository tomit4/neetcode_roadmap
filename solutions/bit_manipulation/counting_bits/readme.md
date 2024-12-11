# 338. Counting Bits

[Counting Bits](https://leetcode.com/problems/counting-bits/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=RyBM56RIWrM)

Given an integer `n`, return <em>an array</em> `ans` <em>of length</em> `n + 1`
<em>such that for each</em> `i (0 <= i <= n)`, `ans[i]` <em>is the <b>number
of</b></em> `1`<em><b>'s in the binary representation of</b></em> `i`.

**Example 1:**

```
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
```

**Example 2:**

```
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 -->11
4 --> 100
5 --> 101
```

**Constraints:**

- `0 <= n <= 10^5`
