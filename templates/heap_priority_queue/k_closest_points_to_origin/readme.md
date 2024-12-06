# 973. K Closest Points to Origin

[K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=rI2EBUEMfTk&pp=ygUjbmVldGNvZGUgSyBDbG9zZXN0IFBvaW50cyB0byBPcmlnaW4%3D)

Given an array of points where `points[i] = [xi, yi]` represents a point on the
<b>X-Y</b> plane and an integer `k`, return the `k` closest points to the origin
`(0, 0)`.

The distance between two points on the <b>X-Y</b> plane is the Euclidean
distance (i.e.,$\sqrt(x1 - x2)^2 + (y1 - y2)^2$).

You may return the answer in <b>any order</b>. The answer is <b>guaranteed</b>
to be <b>unique</b> (except for the order that it is in).

**Example 1:**

<img src="./k_closest_point_to_origin.jpg" />

```
Input:
points = [[1,3],[-2,2]], k = 1
Output:
[[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10). The distance between
(-2, 2) and the origin is sqrt(8). Since sqrt(8) < sqrt(10), (-2, 2) is closer
to the origin. We only want the closest k = 1 points from the origin, so the
answer is just [[-2,2]].
```

**Example 2:**

```
Input:
points = [[3,3],[5,-1],[-2,4]], k = 2
Output:
[[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
```

**Constraints:**

- `1 <= k <= points.length <= 104`
- `-104 <= xi, yi <= 104`
