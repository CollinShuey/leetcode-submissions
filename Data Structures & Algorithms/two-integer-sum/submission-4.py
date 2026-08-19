class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i in range(len(nums)):
            comp = target-nums[i]
            if comp in prev:
                return [prev[comp],i]
            prev[nums[i]] = i
