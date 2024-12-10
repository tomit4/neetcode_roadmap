from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize=3))
    assert (
        solution.isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize=3) == True
    )

    print(solution.isNStraightHand(hand=[1, 2, 3, 4, 5], groupSize=4))
    assert solution.isNStraightHand(hand=[1, 2, 3, 4, 5], groupSize=4) == False
