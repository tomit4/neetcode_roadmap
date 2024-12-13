from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        return ""

    def decode(self, s: str) -> List[str]:
        return [""]


if __name__ == "__main__":
    solution = Solution()

    encoded_1 = solution.encode(strs=["lint", "code", "love", "you"])
    decoded_1 = solution.decode(s=encoded_1)
    print(decoded_1)
    assert decoded_1 == ["lint", "code", "love", "you"]

    encoded_2 = solution.encode(strs=["", ""])
    decoded_2 = solution.decode(s=encoded_2)
    print(decoded_2)
    assert decoded_2 == ["", ""]

    encoded_3 = solution.encode(strs=["hello#", "world#"])
    decoded_3 = solution.decode(s=encoded_3)
    print(decoded_3)
    assert decoded_3 == [
        "hello#",
        "world#",
    ]

    encoded_4 = solution.encode(strs=["test", "", "case", ""])
    decoded_4 = solution.decode(s=encoded_4)
    print(decoded_4)
    assert decoded_4 == [
        "test",
        "",
        "case",
        "",
    ]

    encoded_5 = solution.encode(strs=["weird#string", "contains#hashes", "  spaces  "])
    decoded_5 = solution.decode(s=encoded_5)
    print(decoded_5)
    assert decoded_5 == [
        "weird#string",
        "contains#hashes",
        "  spaces  ",
    ]

    encoded_6 = solution.encode(strs=["###"])
    decoded_6 = solution.decode(s=encoded_6)
    print(decoded_6)
    assert decoded_6 == ["###"]

    long_string = "a" * 100
    encoded_7 = solution.encode(strs=[long_string])
    decoded_7 = solution.decode(s=encoded_7)
    print(decoded_7)
    assert decoded_7 == [long_string]

    encoded_8 = solution.encode(strs=[])
    decoded_8 = solution.decode(s=encoded_8)
    print(decoded_8)
    assert decoded_8 == []
