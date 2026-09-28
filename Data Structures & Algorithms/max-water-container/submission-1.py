class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1


        res = 0
        
        while l < r:
            
            if heights[l] <= heights[r]:
                curr_water = heights[l] * (r-l)
                res = max(res,curr_water)
                l+=1
            elif heights[r] < heights[l]:
                curr_water = heights[r] * (r-l)
                res = max(res,curr_water)
                r -= 1
        
        return res
