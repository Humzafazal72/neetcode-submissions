class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_hash  = {}
        heap = []
        for n in nums:
            freq_hash[n] = freq_hash.get(n,0)+1
        
        for key,val in freq_hash.items():
            if len(heap)<k:
                heapq.heappush(heap,(val,key))
            
            elif heap[0]<(val,key):
                heapq.heappop(heap)
                heapq.heappush(heap,(val,key))
        
        return [key for val,key in heap]
