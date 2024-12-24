from collections import Counter


def sliding_window_with_count(s, t):
    target_count = Counter(t)
    window_count = Counter()
    left = 0
    matches = 0

    for right in range(len(s)):
        char = s[right]
        if char in target_count:
            window_count[char] += 1
            if window_count[char] == target_count[char]:
                matches += 1

        # Shrink the window when it exceeds the length of t
        while right - left + 1 > len(t):
            char = s[left]
            if char in target_count:
                if window_count[char] == target_count[char]:
                    matches -= 1
                window_count[char] -= 1
            left += 1

        if matches == len(target_count):
            return True  # Found a valid window

        return False


# Example Problem
# Problem Check if s2 continues a permutation of s1.
s1 = "ab"
s2 = "eidbaooo"
print(sliding_window_with_count(s2, s1))
# Output: True (substring "ba" is a permuatation of "ab")
