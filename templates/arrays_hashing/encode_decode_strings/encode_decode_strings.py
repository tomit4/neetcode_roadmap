from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        return ""

    def decode(self, s: str) -> List[str]:
        return [""]


if __name__ == "__main__":
    solution = Solution()
    encoded_1 = solution.encode(strs=["list", "code", "love", "you"])
    decoded_1 = solution.decode(s=encoded_1)
    print(decoded_1)
    assert decoded_1 == ["lint", "code", "love", "you"]

    encoded_2 = solution.encode(strs=["we", "say", ":", "yes"])
    decoded_2 = solution.decode(s=encoded_2)
    print(decoded_2)
    assert decoded_2 == ["we", "say", ":", "yes"]
