# 739. Daily Temperatures

[Daily Temperatures](https://leetcode.com/problems/daily-temperatures/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=cTBiBSnjO3c&pp=ygUabmVldGNvZGUgZGFpbHkgdGVtcGVyYXR1cmU%3D)

Given an array of integers `temperatures` represents the daily temperatures,
return <em>an array</em> `answer` <em>such that</em> `answer[i]` <em>is the
number of days you have to wait after the</em> `i`<sup>th</sup> <em>day to get a
warmer temperature</em>. If there is no future day for which this is possible,
keep `answer[i] == 0` instead.

**Example 1:**

```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

**Example 2:**

```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

**Example 3:**

```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

**Constraints:**

- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`
