class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = [ch.lower() for ch in s if ch.isalnum()]

        l, r = 0, len(lst) - 1

        while l < r:
            if lst[l] != lst[r]:
                return False
            else:
                l += 1
                r -= 1

        return True 