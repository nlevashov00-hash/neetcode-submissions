class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq = 0

        set_nums = set(nums)

        for num in nums:
            if num - 1 not in set_nums:
                length = 0

                while num + length in set_nums:
                    length += 1
                longest_seq = max(longest_seq, length)
        
        return longest_seq


                