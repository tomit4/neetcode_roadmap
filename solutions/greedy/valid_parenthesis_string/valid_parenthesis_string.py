class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min, left_max = 0, 0

        for c in s:
            if c == "(":
                left_min, left_max = left_min + 1, left_max + 1
            elif c == ")":
                left_min, left_max = left_min - 1, left_max - 1
            else:  # wildcard
                left_min, left_max = left_min - 1, left_max + 1

            if left_max < 0:
                return False
            if left_min < 0:  # s = ( * ) (
                left_min = 0

        return left_min == 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.checkValidString(s="()"))
    assert solution.checkValidString(s="()") == True

    print(solution.checkValidString(s="(*)"))
    assert solution.checkValidString(s="(*)") == True

    print(solution.checkValidString(s="(*))"))
    assert solution.checkValidString(s="(*))") == True
