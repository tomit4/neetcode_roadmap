from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        return ""

    def decode(self, s: str) -> List[str]:
        return [""]


if __name__ == "__main__":
    solution = Solution()
    encoded = solution.encode(strs=["list", "code", "love", "you"])
    print("encoded :=>", encoded)
    decoded = solution.decode(s=encoded)
    print("Dencoded :=>", decoded)
