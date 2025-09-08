# MinHeap implementation, just inverting values to make it max. O(n log n) time, O(n) space.

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x < y:
                heapq.heappush(stones,x-y)
        if len(stones) == 1:
            return -stones[0]
        return 0