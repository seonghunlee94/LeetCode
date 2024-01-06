import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return heapq.nlargest(k, nums)[-1]
        heapq.heapify(nums)
        
        for _ in range(len(nums)-k):
            print("1")
            heapq.heappop(nums)
        
        return heapq.heappop(nums)