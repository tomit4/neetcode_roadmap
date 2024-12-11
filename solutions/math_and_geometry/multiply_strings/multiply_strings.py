class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])

                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10

        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1

        res = map(str, res[beg:])

        return "".join(res)


if __name__ == "__main__":
    solution = Solution()
    print(solution.multiply(num1="2", num2="3"))
    assert solution.multiply(num1="2", num2="3") == "6"

    print(solution.multiply(num1="123", num2="456"))
    assert solution.multiply(num1="123", num2="456") == "56088"
