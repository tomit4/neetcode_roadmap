# 1584. Min Cost to Connect All Points

[Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=f7JOBJIC-NA&pp=ygUnbmVldGNvZGUgTWluIENvc3QgdG8gQ29ubmVjdCBBbGwgUG9pbnRz)

You are given an array `points` representing integer coordinates of some points
on a 2D-plane, where `points[i] = [x`<sub>i</sub>`, y`<sub>i</sub>`]`.

The cost of connecting two points `[x`<sub>i</sub>`, y`<sub>i</sub>`]` and
`[x`<sub>j</sub>`, y`<sub>j</sub>`]` is the <b>manhattan distance</b> between
them: $|x_i - x_j| + |y_i - y_j|$, where $|val|$ denotes the absolute value of
`val`.

Return <em>the minimum cost to make all points connected</em>. All points are
connected if there is <b>exactly one</b> simple path between any two points.

**Example 1:**

<img src="./min_cost_to_connect_all_points_01.png" />

```
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:
```

<img src="./min_cost_to_connect_all_points_02.png" />

```
We can connect the points as shown above to get the minimum cost of 20. Notice
that there is a unique path between every pair of points.
```

**Example 2:**

```
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
```

**Constraints:**

- `1 <= points.length <= 1000`
- `-10^6 <= x`<sub>i</sub>`, y`<sub>i</sub>`<= 10^6`
- All pairs `(x`<sub>i</sub>`, y`<sub>i</sub>`)` are distinct.
