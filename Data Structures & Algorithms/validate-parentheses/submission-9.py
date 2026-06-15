class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for ch in s:
            if ch in dictionary:
                stack.append(ch)
            elif stack and ch == dictionary[stack[-1]]:
                stack.pop()
            else:
                return False
        
        if not stack:
            return True
        else:
            return False
