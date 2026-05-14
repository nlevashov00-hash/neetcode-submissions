class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = collections.defaultdict(int)
        longest_str = 0
        l = 0

        for r in range(len(s)):
            counter[s[r]] += 1

            while (r - l + 1) - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1
            
            longest_str = max(longest_str, (r - l + 1))
        
        return longest_str

