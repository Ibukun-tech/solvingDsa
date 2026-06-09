import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         # Step 1: Build frequency HashMap
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1

    # Step 2: Maintain min heap of size k
        heap = []
        for num, frequency in hashmap.items():
            heapq.heappush(heap, (frequency, num))
        
            if len(heap) > k:
                heapq.heappop(heap)

    # Step 3: Extract results
        return [num for frequency, num in heap]