class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return ""


if __name__ == "__main__":
    solution = Solution()
    print(solution.multiply(num1="2", num2="3"))
    assert solution.multiply(num1="2", num2="3") == "6"

    print(solution.multiply(num1="123", num2="456"))
    assert solution.multiply(num1="123", num2="456") == "56088"
