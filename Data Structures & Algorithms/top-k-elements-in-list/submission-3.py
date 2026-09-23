class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        col = {}
        output = []
        for num in nums:
            col[num] = 1 + col.get(num,0)
        

        bucket = [[] for _ in range(len(nums) + 1)]
        [1,2,3,3]

        for key,val in col.items():
            bucket[val].append(key)
        

        for i in range(len(bucket)-1,-1,-1):
            if k == 0:
                return output
            for num in bucket[i]:
                k -=1
                output.append(num)
            