import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = defaultdict(int)
        for n in nums:
            table[n] += 1
        counts = [[value, key] for key, value in table.items()]
        minHeap = []
        for count in counts:
            heapq.heappush(minHeap,count)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
            
        return [c[1] for c in minHeap]
        