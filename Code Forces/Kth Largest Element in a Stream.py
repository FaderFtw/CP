import heapq

class KthLargest:

    def __init__(self, k: int, nums):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)

        print(self.minHeap)
        while self.k < len(self.minHeap):
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
            
        return self.minHeap[0]
    
stream = KthLargest(3,[4, 5, 8, 2])
print(stream.add(5))