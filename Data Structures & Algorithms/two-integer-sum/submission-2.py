class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in nums and nums.index(difference) != i:
                result.append(i)
                result.append(nums.index(difference))
                result.sort()
                return result
            