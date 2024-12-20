# 1851. Minimum Interval to Include Each Query

[Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=5hQ5WWW5awQ&pp=ygUvbmVldGNvZGUgTWluaW11bSBJbnRlcnZhbCB0byBJbmNsdWRlIEVhY2ggUXVlcnk%3D)

You are given a 2D integer array `intervals`, where
`intervals[i] = [left`<sub>i</sub>`, right`<sub>i</sub>`]` describes the
`i`<sub>th</sub> interval starting at `left`<sub>i</sub> and ending at
`right`<sub>i</sub> (<b>inclusive</b>). The <b>size</b> of an interval is
defined as the number of integers it contains, or more formally
`right`<sub>i</sub>`-
left`<sub>i</sub>`+ 1`.

You are also given an integer array `queries`. The answer to the
`j`<sup>th</sup> query is the <b>size of the smallest interval</b> `i` such that
`left`<sub>i</sub>`<= queries[j] <= right`<sub>i</sub>. If no such interval
exists, the answer is `-1`.

Return <em>an array containing the answers to the queries.</em>

**Example 1:**

```
Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
Explanation: The queries are processed as follows:

- Query = 2: The interval [2,4] is the smallest interval containing 2. The
  answer is 4 - 2 + 1 = 3.
- Query = 3: The interval [2,4] is the smallest interval containing 3. The
  answer is 4 - 2 + 1 = 3.
- Query = 4: The interval [4,4] is the smallest interval containing 4. The
  answer is 4 - 4 + 1 = 1.
- Query = 5: The interval [3,6] is the smallest interval containing 5. The
  answer is 6 - 3 + 1 = 4.
```

**Example 2:**

```
Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
Output: [2,-1,4,6]
Explanation: The queries are processed as follows:

- Query = 2: The interval [2,3] is the smallest interval containing 2. The
  answer is 3 - 2 + 1 = 2.
- Query = 19: None of the intervals contain 19. The answer is -1.
- Query = 5: The interval [2,5] is the smallest interval containing 5. The
  answer is 5 - 2 + 1 = 4.
- Query = 22: The interval [20,25] is the smallest interval containing 22. The
  answer is 25 - 20 + 1 = 6.
```

**Constraints:**

- `1 <= intervals.length <= 10^5`
- `1 <= queries.length <= 10^5`
- `intervals[i].length == 2`
- `1 <= left`<sub>i</sub>`<= right`<sub>i</sub>`<= 10^7`
- `1 <= queries[j] <= 10^7`
