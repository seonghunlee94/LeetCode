import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []
        
        for num in nums:
            heapq.heappush(heap, -num)
        
        
        for _ in range(k):
            largest_k_th = heapq.heappop(heap)
        
        
        return -largest_k_th

        
        
        
        