import heapq
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # O(n*logn)
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]

            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize=3))
    assert (
        solution.isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize=3) == True
    )

    print(solution.isNStraightHand(hand=[1, 2, 3, 4, 5], groupSize=4))
    assert solution.isNStraightHand(hand=[1, 2, 3, 4, 5], groupSize=4) == False
