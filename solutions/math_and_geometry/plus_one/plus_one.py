from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        one, i = 1, 0

        while one == 1:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
            i += 1

        return digits[::-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne(digits=[1, 2, 3]))
    assert solution.plusOne(digits=[1, 2, 3]) == [1, 2, 4]

    print(solution.plusOne(digits=[4, 3, 2, 1]))
    assert solution.plusOne(digits=[4, 3, 2, 1]) == [4, 3, 2, 2]

    print(solution.plusOne(digits=[9]))
    assert solution.plusOne(digits=[9]) == [1, 0]
