# 518. Coin Change II

[Coin Change II](https://leetcode.com/problems/coin-change-ii/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=Mjy4hd2xgrs&pp=ygUXbmVldGNvZGUgQ29pbiBDaGFuZ2UgSUk%3D)

You are given an integer array `coins` representing coins of different
denominations and an integer amount representing a total `amount` of money.

Return <em>the number of combinations that make up that amount.</em> If that
amount of money cannot be made up by any combination of the coins, return `0`.

You may assume that you have an infinite number of each kind of coin.

The answer is <b>guaranteed</b> to fit into a signed <b>32-bit</b> integer.

**Example 1:**

```
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```

**Example 2:**

```
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
```

**Example 3:**

```
Input: amount = 10, coins = [10]
Output: 1
```

**Constraints:**

- `1 <= coins.length <= 300`
- `1 <= coins[i] <= 5000`
- All the values of `coins` are <b>unique.</b>
- `0 <= amount <= 5000`
