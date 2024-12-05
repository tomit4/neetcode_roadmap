# 39. Combination Sum

[Combination Sum](https://leetcode.com/problems/combination-sum/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=GBKI9VSKdGg&pp=ygUYbmVldGNvZGUgQ29tYmluYXRpb24gU3Vt)

Given an array of <b>distinct</b> integers `candidates` and a target integer
`target`, return <em>a list of all <b>unique combinations</b> of `candidates`
where the chosen numbers sum to</em> `target`. You may return the combinations
in <b>any order.</b>

The <b>same</b> number may be chosen from `candidates` an <b>unlimited number of
times</b>. Two combinations are unique if the frequency (the <b>frequency</b> of
the number `x` is the number of times it occurs in the array) of at least one of
the chosen numbers is different.

The test cases are generated such that the number of unique combinations that
sum up to `target` is less than `150` combinations for the given input.

**Example 1:**

```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7. These are the only two combinations.
```

**Example 2:**

```
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

**Example 3:**

```
Input: candidates = [2], target = 1
Output: []
```

**Constraints:**

- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- All elements of `candidates` are <b>distinct.</b>
- `1 <= target <= 40`
