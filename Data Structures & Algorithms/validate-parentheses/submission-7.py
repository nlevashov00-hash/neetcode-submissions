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
                last_ch = stack.pop()
                if dictionary[last_ch] != ch:
                    return False

        return len(stack) == 0 