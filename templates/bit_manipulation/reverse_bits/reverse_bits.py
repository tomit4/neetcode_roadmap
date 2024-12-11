class Solution:
    def reverseBits(self, n: int) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()
    n_1 = int("00000010100101000001111010011100", 2)
    print(solution.reverseBits(n=n_1))
    assert solution.reverseBits(n=n_1) == 964176192

    n_2 = int("11111111111111111111111111111101", 2)
    print(solution.reverseBits(n=n_2))
    assert solution.reverseBits(n=n_2) == 3221225471
