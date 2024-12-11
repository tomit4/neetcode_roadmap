class Solution:
    def isPalindrome(self, s: str) -> bool:
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(s="A man, a plan, a canal: Panama"))
    assert solution.isPalindrome(s="A man, a plan, a canal: Panama") == True

    print(solution.isPalindrome(s="race a car"))
    assert solution.isPalindrome(s="race a car") == False

    print(solution.isPalindrome(s=" "))
    assert solution.isPalindrome(s=" ") == True
