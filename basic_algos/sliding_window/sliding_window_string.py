def sliding_window_string(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


# Example Problem
# Problem: Find the length of the longest substring with unique characters
s = "abcabcbb"
print(sliding_window_string(s))
# Output: 3 (substring "abc")
