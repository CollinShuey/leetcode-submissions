class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = r = 0

        for i in range(len(cost)-1,-1,-1):
            cost[i] = cost[i] + min(l,r)
            r = l
            l = cost[i]

        return min(l,r)

        