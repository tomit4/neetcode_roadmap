from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visit = {}  # False=visited, True=visited & current path
        res = []

        def depth_first_search(c):
            if c in visit:
                return visit[c]

            visit[c] = True

            for nei in adj[c]:
                if depth_first_search(nei):
                    return True

            visit[c] = False
            res.append(c)

        for c in adj:
            if depth_first_search(c):
                return ""

        res.reverse()
        return "".join(res)


if __name__ == "__main__":
    solution = Solution()
    print(solution.foreignDictionary(words=["z", "o"]))
    assert solution.foreignDictionary(words=["z", "o"]) == "zo"

    print(solution.foreignDictionary(words=["hrn", "hrf", "er", "enn", "rfnn"]))
    assert (
        solution.foreignDictionary(words=["hrn", "hrf", "er", "enn", "rfnn"]) == "hernf"
    )
