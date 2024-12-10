from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        return []


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
