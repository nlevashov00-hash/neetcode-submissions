class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = collections.defaultdict(int)

        for num in nums:

            if dictionary[num] > 0:
                return True
            dictionary[num] += 1
        
        return False
            