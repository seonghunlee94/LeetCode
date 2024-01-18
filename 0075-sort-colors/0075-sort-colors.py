class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        if len(nums) == 1:
            return nums
        
        
        def partition(part, ps, pe):
            # 피벗 정하기
            pivot = part[pe]
            i = ps - 1
            
            # 피벗 정렬
            for j in range(ps, pe):
                if part[j] <= pivot:
                    i += 1
                    part[i], part[j] = part[j], part[i]
            
            # 정렬 후 피벗 위치 정해주기
            part[i + 1], part[pe] = part[pe], part[i + 1]
            return i + 1
        
        
        def quicksort(lst, start, end):
            # 베이스 케이스
            if start >= end:
                return None
            
            # 파티션 나누기
            p = partition(lst, start, end)
            
            # 재귀 호출
            quicksort(lst, start, p-1)
            quicksort(lst, p, end)
            
            return lst
            
            
        quicksort(nums, 0, len(nums) - 1)