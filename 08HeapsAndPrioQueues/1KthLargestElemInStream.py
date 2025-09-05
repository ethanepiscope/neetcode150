# O(log k) time per add, O(k) space

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        self.heap_len = 0
        for num in nums:
            self.add(num)                

    def add(self, val: int) -> int:
        if self.heap_len < self.k:
            heapq.heappush(self.heap, val)
            self.heap_len += 1
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap,val)
        return self.heap[0]
