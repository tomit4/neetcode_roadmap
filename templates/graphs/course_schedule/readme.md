# 207. Course Schedule

[Course Schedule](https://leetcode.com/problems/course-schedule/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=EgI5nU9etnU&pp=ygUYbmVldGNvZGUgQ291cnNlIFNjaGVkdWxl)

There are a total of `numCourses` courses you have to take, labeled from `0` to
`numCourses - 1`. You are given an array `prerequisites` where
`prerequisites[i] = [ai, bi]` indicates that you <b>must</b> take course
`b`<sub>`i`</sub> first if you want to take course `a`<sub>`i`</sub>.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to
  first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

**Example 1:**

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. To take course 1 you should
have finished course 0. So it is possible.
```

**Example 2:**

```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. To take course 1 you should have
finished course 0, and to take course 0 you should also have finished course 1.
So it is impossible.
```

**Constraints:**

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= ai, bi < numCourses`
- All the pairs `prerequisites[i]` are <b>unique</b>.
