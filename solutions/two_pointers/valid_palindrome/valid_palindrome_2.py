class Solution:
    def isPalindrome(self, s: str) -> bool:
        left: int = 0
        right: int = len(s) - 1

        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while right > left and not self.alphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True

    def alphaNum(self, c: str) -> bool:
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(s="A man, a plan, a canal: Panama"))
    print(solution.isPalindrome(s="race a car"))
    print(solution.isPalindrome(s=" "))
