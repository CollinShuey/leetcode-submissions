class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2

        l = 0
        r = len(nums) - 1


        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid-1
                
            elif target > nums[mid]:
                l = mid+1
            print(l,r)




        return -1
        