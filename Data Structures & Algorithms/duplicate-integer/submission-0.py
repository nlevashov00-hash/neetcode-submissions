class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:
        dct = {}

        for n in nums:
            if n not in dct:
                dct[n] = 1
            else:
                return True

        return False