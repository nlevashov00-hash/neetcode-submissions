class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        res = []

        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue    

            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                elif s > 0:
                    k -= 1
                else:
                    j += 1
        
        return res
