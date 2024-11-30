class Solution:
    def isPalindrome(self, s: str) -> bool:
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(s="A man, a plan, a canal: Panama"))
    print(solution.isPalindrome(s="race a car"))
    print(solution.isPalindrome(s=" "))
