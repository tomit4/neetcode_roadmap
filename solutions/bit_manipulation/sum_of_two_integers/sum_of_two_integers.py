class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Mask to get 32-bit integer representation
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        while b != 0:
            #  XOR to add without carry
            temp = (a & b) << 1  # Carry
            a = (a ^ b) & MASK  # Add without carry, mask to 32 bits
            b = temp & MASK  # Carry, mask to 32 bits

        # If the result is negative in a 32-bit signed integer, convert it
        return a if a <= INT_MAX else ~(a ^ MASK)


if __name__ == "__main__":
    solution = Solution()
    print(solution.getSum(a=1, b=2))
    assert solution.getSum(a=1, b=2) == 3

    print(solution.getSum(a=2, b=3))
    assert solution.getSum(a=2, b=3) == 5
