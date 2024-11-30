# 167. Two Sum II - Input Array Is Sorted

[Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=cQ1Oz4ckceM&pp=ygUqbmVldGNvZGUgdHdvIHN1bSB0d28gaW5wdXQgYXJyYXkgaXMgc29ydGVk)

Given a <b>1-indexed</b> array of integers `numbers` that is already
<b><em>sorted in non-decreasing order</em></b>, find two numbers such that they
add up to a specific `target` number. Let these two numbers be `numbers[index1]`
and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return <em>the indices of the two numbers</em>, `index1` and `index2`,
<b><em>added by one</b> as an integer array</em> `[index1, index2]` <em>of
length 2</em>.

The tests are generated such that there is <b>exactly one solution</b>. You
<b>may not</b> use the same element twice.

Your solution must use only constant extra space.

**Example 1:**

```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```

**Example 2:**

```
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
```

**Example 3:**

```
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
```

**Constraints:**

- `2 <= numbers.length <= 3 * 104`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in <b>non-decreasing order</b>.
- `-1000 <= target <= 1000`
- The tests are generated such that there is <b>exactly one solution</b>.
