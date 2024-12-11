import math


class Solution:
    def reverse(self, x: int) -> int:
        # Integer.MAX_VALUE = 2147483647 (ends with 7)
        # Integer.MIN_VALUE = -2147483648 (ends with -8)

        MIN = -2147483648  # -2^31
        MAX = 2147483647  # 2^31 - 1

        res = 0
        while x:
            digit = int(math.fmod(x, 10))  # (python dumb) -1 % 10 = 9
            x = int(x / 10)  # (python dumb) -1 // 10 = -1

            if res > MAX // 10 or (res == MAX // 10 and digit >= MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit <= MIN % 10):
                return 0
            res = (res * 10) + digit

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(x=123))
    assert solution.reverse(x=123) == 321

    print(solution.reverse(x=-123))
    assert solution.reverse(x=-123) == -321

    print(solution.reverse(x=120))
    assert solution.reverse(x=120) == 21
