class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        # 서로 순서를 바꿔 더한 값이 높은지 구하는 함수 
        def to_swap(n1, n2):
            return str(n1) + str(n2) < str(n2) + str(n1)
        
        
        i = 1
        while i < len(nums):
            j = i
            
            while j > 0 and to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            
            i += 1
            
        return str(int(''.join(map(str, nums))))
        
        
        
        
        
        
        
        
        
        
#         if not nums:
#             return
        
#         iters = len(nums)-1
#         # 인덱스 정렬(맨 앞자리의 숫자가 클 시, 앞으로 작을 시 그 자리에.)
#         for iter in range(iters):
#             wall = iters - iter
#             for cur in range(wall):
#                 if str(nums[cur])[-1] == '0':
#                     if str(nums[cur])[0:-1] < str(nums[cur + 1]):
#                         nums[cur], nums[cur + 1] = nums[cur + 1], nums[cur]
#                 elif str(nums[cur+1])[-1] == '0':
#                     if str(nums[cur]) < str(nums[cur + 1])[0:-1]:
#                         nums[cur], nums[cur + 1] = nums[cur + 1], nums[cur]
#                 elif str(nums[cur]) < str(nums[cur + 1]):
#                     nums[cur], nums[cur + 1] = nums[cur + 1], nums[cur]

#         total_sum = ''
#         for num in nums:
#             total_sum += f"{num}"
            
#         return total_sum
                
        
        