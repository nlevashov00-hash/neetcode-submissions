class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:
        integers = set()

        for i in nums:
            if i not in integers:
                integers.add(i)
            else:
                return True

        return False 