# 684. Redundant Connection

[Redundant Connection](https://leetcode.com/problems/redundant-connection/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=FXWRE67PLL0&pp=ygUdbmVldGNvZGUgUmVkdW5kYW50IENvbm5lY3Rpb24%3D)

In this problem, a tree is an <b>undirected graph</b> that is connected and has
no cycles.

You are given a graph that started as a tree with `n` nodes labeled from `1` to
`n`, with one additional edge added. The added edge has two <b>different</b>
vertices chosen from `1` to `n`, and was not an edge that already existed. The
graph is represented as an array `edges` of length n where
`edges[i] = [a`<sub>`i`</sub>`, b`<sub>i</sub>`]` indicates that there is an
edge between nodes `a`<sub>i</sub> and `b`<sub>i</sub> in the graph.

Return <em>an edge that can be removed so that the resulting graph is a tree
of</em> `n`
<em>nodes.</em> If there are multiple answers, return the answer that occurs
last in the input.

**Example 1:**

<img src="./redundant_connection_01.jpg" />

```
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
```

**Example 2:**

```
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
```

**Constraints:**

- `n == edges.length`
- `3 <= n <= 1000`
- `edges[i].length == 2`
- `1 <= ai < bi <= edges.length`
- `ai != bi`
- There are no repeated edges.
- The given graph is connected.
