from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]  # array of empty arrays [ [], [] ...]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # items() creates tuples from dict, first is num itself, c is freqency
        # at the list living at index c, we append the number itself
        for n, c in count.items():
            freq[c].append(n)

        res = []
        # in the range of len(freq -1), starting from the last index (-1)
        # going to the first element 0
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res

    # Time complexity: O(n)


if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
    assert sorted(solution.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2)) == sorted([1, 2])

    print(solution.topKFrequent(nums=[1], k=1))
    assert sorted(solution.topKFrequent(nums=[1], k=1)) == sorted([1])

    print(solution.topKFrequent(nums=[-1, -1], k=1))
    assert sorted(solution.topKFrequent(nums=[-1, -1], k=1)) == sorted([-1])

    print(solution.topKFrequent(nums=[4, 1, -1, 2, -1, 2, 3], k=2))
    assert sorted(solution.topKFrequent(nums=[4, 1, -1, 2, -1, 2, 3], k=2)) == sorted(
        [-1, 2]
    )
