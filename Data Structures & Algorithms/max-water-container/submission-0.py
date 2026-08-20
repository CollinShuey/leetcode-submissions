class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0

        l,r = 0,len(height)-1

        while l < r:
            volume = min(height[l],height[r]) * (r-l)
            max_water = max(max_water, volume)
            if height[l] <= height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            
        return max_water

        