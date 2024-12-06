# 127. Word Ladder

[Word Ladder](https://leetcode.com/problems/word-ladder/description/)

[Neetcode Solution](https://www.youtube.com/watch?v=h9iTnkgv05E&pp=ygUUbmVldGNvZGUgV29yZCBMYWRkZXI%3D)

A <b>transformation sequence</b> from word `beginWord` to word `endWord` using a
dictionary `wordList` is a sequence of words
`beginWord -> s`<sub>`1`</sub>`-> s`<sub>`2`</sub>`-> ... ->
s`<sub>`k`</sub>
such that:

- Every adjacent pair of words differs by a single letter.
- Every `s`<sub>`i`</sub> for `1 <= i <= k` is in `wordList`. Note that
  `beginWord` does not need to be in `wordList`.
- `sk == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return
<em>the <b>number of words</b> in the <b>shortest transformation sequence</b>
from</em> `beginWord` <em>to</em> `endWord`, <em>or</em> `0` <em>if no such
sequence exists.</em>

**Example 1:**

```
Input: beginWord = "hit", endWord = "cog", wordList =
["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5
words long.
```

**Example 2:**

```
Input: beginWord = "hit", endWord = "cog", wordList =
["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
```

**Constraints:**

- `1 <= beginWord.length <= 10`
- `endWord.length == beginWord.length`
- `1 <= wordList.length <= 5000`
- `wordList[i].length == beginWord.length`
- `beginWord`, `endWord`, and `wordList[i]` consist of lowercase English
  letters.
- `beginWord != endWord`
- All the words in `wordList` are <b>unique.</b>
