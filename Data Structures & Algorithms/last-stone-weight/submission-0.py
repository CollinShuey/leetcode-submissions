class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]

        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x, y = -(heapq.heappop(max_heap)),-(heapq.heappop(max_heap))
            if x > y:
                x -= y
                heapq.heappush(max_heap,-x)
            elif y > x:
                y -= x
                heapq.heappush(max_heap,-y)
            else:
                continue

        

        if max_heap:
            return -(max_heap[0])
        return 0