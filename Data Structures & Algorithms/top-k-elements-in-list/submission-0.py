class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        col = {}


        for num in nums:
            col[num] = 1 + col.get(num,0)
        

        bucket = [[] for i in range(len(nums)+ 1)] 

        for num, cnt in col.items():
            bucket[cnt].append(num)
        res = []
        count = 0
        for i in reversed(range(len(bucket))):
            for j in bucket[i]:
                count += 1
                res.append(j)
                if count == k:
                    return res
        


