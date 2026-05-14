class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        dictionary = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []

        for ch in s:

            if ch in dictionary:
                stack.append(ch)
            elif not stack:
                return False
            else:
                if dictionary[stack[-1]] == ch:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        else:
            return False  