# 417. Pacific Atlantic Water Flow

[Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=s-VkcjHqkGI&pp=ygUkbmVldGNvZGUgUGFjaWZpYyBBdGxhbnRpYyBXYXRlciBGbG93)

There is an `m x n` rectangular island that borders both the <b>Pacific
Ocean</b> and <b>Atlantic Ocean</b>. The <b>Pacific Ocean</b> touches the
island's left and top edges, and the <b>Atlantic Ocean</b> touches the island's
right and bottom edges.

The island is partitioned into a grid of square cells. You are given an `m x n`
integer matrix `heights` where `heights[r][c]` represents the <b>height above
sea level</b> of the cell at coordinate `(r, c)`.

The island receives a lot of rain, and the rain water can flow to neighboring
cells directly north, south, east, and west if the neighboring cell's height is
<b>less than or equal to</b> the current cell's height. Water can flow from any
cell adjacent to an ocean into the ocean.

Return a <em><b>2D list</b> of grid coordinates</em> `result` <em>where</em>
`result[i] = [ri, ci]` <em>denotes that rain water can flow from cell</em>
`(ri, ci)` to <b>both</b> the Pacific and Atlantic oceans.</em>

**Example 1:**

<img src="./pacific_atlantic_water_flow.jpg" />

```
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific ocean
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
```

**Example 2:**

```
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
```

**Constraints:**

- `m == heights.length`
- `n == heights[r].length`
- `1 <= m, n <= 200`
- `0 <= heights[r][c] <= 10^5`
