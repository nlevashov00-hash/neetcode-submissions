class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()
        l, r = 0, 0
        longest_str = 0

        while r <= len(s) - 1:
            ch = s[r]

            if ch not in count:
                count.add(ch)
                r += 1
                longest_str = max(longest_str, r - l)
            else:
                count.remove(s[l])
                l += 1

        return longest_str