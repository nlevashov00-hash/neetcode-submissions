class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        dict_1 = collections.defaultdict(int)
        dict_2 = collections.defaultdict(int)
        l, r = 0, len(s1) - 1

        for ch in s1:
            dict_1[ch] += 1
        
        for c in s2[:len(s1)]:
            dict_2[c] += 1
        
        if dict_1 == dict_2:
            return True
        else:
            while r < len(s2) - 1:
                dict_2[s2[l]] -= 1
                if dict_2[s2[l]] == 0:
                    del dict_2[s2[l]]     
                l += 1
                r += 1
                dict_2[s2[r]] += 1
                if dict_1 == dict_2:
                    return True
        
        return False
                


            