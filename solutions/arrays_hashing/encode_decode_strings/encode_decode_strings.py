from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        res: str = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res: List[str] = []
        i: int = 0

        while i < len(s):
            j: int = i
            while s[j] != "#":
                j += 1
            length: int = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return res


if __name__ == "__main__":
    solution = Solution()
    encoded = solution.encode(strs=["list", "code", "love", "you"])
    print("encoded :=>", encoded)
    decoded = solution.decode(s=encoded)
    print("Dencoded :=>", decoded)
