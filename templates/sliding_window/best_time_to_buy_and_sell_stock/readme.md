# 121. Best Time to Buy and Sell Stock

[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=1pkOgXD63yU&pp=ygUobmVldGNvZGUgYmVzdCB0aW1lIHRvIGJ1eSBhbmQgc2VsbCBzdG9jaw%3D%3D)

You are given an array `prices` where `prices[i]` is the price of a given stock
on the `i`<sup>th</sup> day.

You want to maximize your profit by choosing a <b>single day</b> to buy one
stock and choosing a <b>different day in the future</b> to sell that stock.

Return the <em>maximum profit you can achieve from this transaction</em>. If you
cannot achieve any profit, return `0`.

**Example 1:**

```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before
you sell.
```

**Example 2:**

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

**Constraints:**

- `1 <= prices.length <= 105`
- `0 <= prices[i] <= 104`
