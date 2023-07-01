class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = []
        longest_length = 0
        left = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.append(s[right])
            longest_length = max(longest_length, right - left + 1)

        return longest_length