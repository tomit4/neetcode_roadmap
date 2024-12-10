class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
    assert solution.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac") == True

    print(solution.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
    assert solution.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc") == False

    print(solution.isInterleave(s1="", s2="", s3=""))
    assert solution.isInterleave(s1="", s2="", s3="") == True
