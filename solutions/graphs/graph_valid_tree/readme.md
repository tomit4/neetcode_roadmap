# 261. Graph Valid Tree

[Graph Valid Tree](https://neetcode.io/problems/valid-tree)

[Neetcode Solution](https://www.youtube.com/watch?v=bXsUuownnoQ&pp=ygUZbmVldGNvZGUgR3JhcGggVmFsaWQgVHJlZQ%3D%3D)

Given `n` nodes labeled from `0` to `n - 1` and a list of <b>undirected</b>
edges (each edge is a pair of nodes), write a function to check whether these
edges make up a valid tree.

**Example 1:**

```
Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output:
true
```

**Example 2:**

```
Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false
```

**Note:**

- You can assume that no duplicate edges will appear in edges. Since all edges
  are `undirected`, `[0, 1]` is the same as `[1, 0]` and thus will not appear
  together in edges.

**Constraints:**

- `1 <= n <= 100`
- `0 <= edges.length <= n * (n - 1) / 2`
