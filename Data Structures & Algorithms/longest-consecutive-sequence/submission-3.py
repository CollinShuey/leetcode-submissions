class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)

        possible = []
        for n in nums:
            if n-1 not in nset:
                possible.append(n)
        max_length = 0
        curr = 1
        for num in possible:
            n = num
            while n+1 in nset:
                n += 1
                curr += 1
            max_length = max(curr,max_length)
            curr = 1

            


        return max_length
        