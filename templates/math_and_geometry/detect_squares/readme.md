# 2013. Detect Squares

[Detect Squares](https://leetcode.com/problems/detect-squares/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=bahebearrDc&pp=ygUXbmVldGNvZGUgRGV0ZWN0IFNxdWFyZXM%3D)

You are given a stream of points on the X-Y plane. Design an algorithm that:

- <b>Adds</b> new points from the stream into a data structure. <b>Duplicate</b>
  points are allowed and should be treated as different points.
- Given a query point, <b>counts</b> the number of ways to choose three points
  from the data structure such that the three points and the query point form an
  <b>axis-aligned square</b> with <b>positive area.</b>

An <b>axis-aligned square</b> is a square whose edges are all the same length
and are either parallel or perpendicular to the x-axis and y-axis.

Implement the `DetectSquares` class:

- `DetectSquares()` Initializes the object with an empty data structure.
- `void add(int[] point)` Adds a new point `point = [x, y]` to the data
  structure.
- `int count(int[] point)` Counts the number of ways to form <b>axis-aligned
  squares</b> with point `point = [x, y]` as described above.

**Example 1:**

<img src="./detec_squares.png" />

```
Input ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11,
10]]]

Output [null, null, null, null, 1, 0, null, 2]

Explanation
DetectSquares detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
detectSquares.count([11, 10]); // return 1. You can choose:
                               // - The first, second, and third points
detectSquares.count([14, 8]);  // return 0. The query point cannot form a
                               // square with any points in the data structure.
detectSquares.add([11, 2]); // Adding duplicate points is allowed.
detectSquares.count([11, 10]); // return 2. You can choose:
                               // - The first, second, and third points
                               // - The first, third, and fourth points
```

**Constraints:**

- `point.length == 2`
- `0 <= x, y <= 1000`
- At most `3000` calls <b>in total</b> will be made to `add` and `count`.
