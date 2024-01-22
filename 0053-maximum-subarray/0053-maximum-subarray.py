class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        best_sum = -sys.maxsize
        current_sum = 0
        
        # 최대 합계를 구하는 함수
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
            
        return best_sum