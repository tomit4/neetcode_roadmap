class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}

        # k = i + j
        def depth_first_search(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in dp:
                return dp[(i, j)]

            if i < len(s1) and s1[i] == s3[i + j] and depth_first_search(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[i + j] and depth_first_search(i, j + 1):
                return True

            dp[(i, j)] = False
            return False

        return depth_first_search(0, 0)


if __name__ == "__main__":
    solution = Solution()
    print(solution.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
    assert solution.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac") == True

    print(solution.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
    assert solution.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc") == False

    print(solution.isInterleave(s1="", s2="", s3=""))
    assert solution.isInterleave(s1="", s2="", s3="") == True
