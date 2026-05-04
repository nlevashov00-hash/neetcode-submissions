class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = collections.defaultdict(int)
        dict_t = collections.defaultdict(int)

        for ch in s:
            dict_s[ch] += 1
        
        for ch in t:
            dict_t[ch] += 1
        
        return dict_t == dict_s