class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding_str = ""
        
        for s in strs:
            encoding_str += str(len(s)) + "#" + s

        return encoding_str 


    def decode(self, s: str) -> List[str]:
        res = []
        l, r = [0] * 2

        while r < len(s):

            while s[r] != "#":
                r += 1
            
            length_str = int(s[l:r])
            l = r + 1
            r += length_str + 1
            res.append(s[l: r])
            l = r
        
        return res
