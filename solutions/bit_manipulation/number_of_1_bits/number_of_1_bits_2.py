class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.hammingWeight(n=11))
    assert solution.hammingWeight(n=11) == 3

    print(solution.hammingWeight(n=128))
    assert solution.hammingWeight(n=128) == 1

    print(solution.hammingWeight(n=2147483645))
    assert solution.hammingWeight(n=2147483645) == 30
