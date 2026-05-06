class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_sum = 0
        l, r = 0, len(heights) - 1

        while l < r:
            v = min(heights[l], heights[r]) * (r - l)
            max_sum = max(max_sum, v)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_sum

