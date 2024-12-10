from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}

        tickets.sort()

        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]

        def depth_first_search(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)

                if depth_first_search(v):
                    return True

                adj[src].insert(i, v)
                res.pop(v)

            return False

        depth_first_search("JFK")

        return res


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.findItinerary(
            tickets=[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        )
    )
    assert solution.findItinerary(
        tickets=[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    ) == ["JFK", "MUC", "LHR", "SFO", "SJC"]

    print(
        solution.findItinerary(
            tickets=[
                ["JFK", "SFO"],
                ["JFK", "ATL"],
                ["SFO", "ATL"],
                ["ATL", "JFK"],
                ["ATL", "SFO"],
            ]
        )
    )
    assert solution.findItinerary(
        tickets=[
            ["JFK", "SFO"],
            ["JFK", "ATL"],
            ["SFO", "ATL"],
            ["ATL", "JFK"],
            ["ATL", "SFO"],
        ]
    ) == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
