class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        dict_1 = collections.defaultdict(int)
        dict_2 = collections.defaultdict(int)

        for i in range(len(t)):
            dict_1[s[i]] += 1
            dict_2[t[i]] += 1
        
        return dict_1 == dict_2