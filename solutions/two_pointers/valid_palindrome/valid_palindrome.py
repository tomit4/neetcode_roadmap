class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr: str = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()

        return newStr == newStr[::-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(s="A man, a plan, a canal: Panama"))
    print(solution.isPalindrome(s="race a car"))
    print(solution.isPalindrome(s=" "))
