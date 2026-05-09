class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        maping = {
            "(": ")", 
            "{": "}", 
            "[": "]"}

        for ch in s:
            if ch in maping:
                stack.append(ch)
            
            elif not stack:
                return False
            
            else:
                last_ch = stack.pop()
                if maping[last_ch] != ch:
                    return False
        
        return len(stack) == 0


        