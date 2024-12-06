# 210. Course Schedule II

[Course Schedule II](https://leetcode.com/problems/course-schedule-ii/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=Akt3glAwyfY&pp=ygUbbmVldGNvZGUgQ291cnNlIFNjaGVkdWxlIElJ)

There are a total of `numCourses` courses you have to take, labeled from `0` to
`numCourses - 1`. You are given an array `prerequisites` where
`prerequisites[i]
= [ai, bi]` indicates that you <b>must</b> take
course``b`<sub>`i`</sub>
first if you want to take course`a`<sub>`i`</sub>.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to
  first take course `1`.

Return <em>the ordering of courses you should take to finish all courses</em>.
If there are many valid answers, return <b>any</b> of them. If it is impossible
to finish all courses, return <b>an empty array.</b>

**Example 1:**

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should
have finished course 0. So the correct course order is [0,1].
```

**Example 2:**

```
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3
you should have finished both courses 1 and 2. Both courses 1 and 2 should be
taken after you finished course 0. So one correct course order is [0,1,2,3].
Another correct ordering is [0,2,1,3].
```

**Example 3:**

```
Input: numCourses = 1, prerequisites = []
Output: [0]
```

**Constraints:**

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= numCourses * (numCourses - 1)`
- `prerequisites[i].length == 2`
- `0 <= ai, bi < numCourses`
- `ai != bi`
- All the pairs `[ai, bi]` are distinct.
