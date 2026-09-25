class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        n = len(nums)
        res = [1] * n
        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix = nums[i] * prefix
        
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix = nums[i] * postfix
        
        return res
        
