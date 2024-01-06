class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_two = heapq.nlargest(2,list(nums))
        return (max_two[0] - 1) * (max_two[1] - 1)