class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        symbols_set = set()
        l, r = [0] * 2

        while r < len(s):

            if s[r] not in symbols_set:
                symbols_set.add(s[r])
                r += 1
                max_len = max(max_len, r - l)
            else:
                symbols_set.remove(s[l])
                l += 1

        return max_len