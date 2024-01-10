class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        
        def dfs(elements):
            if len(elements) == 0:
                results.append(prev_elements[:])
        
        
            for e in elements:
                next_elements = elements[:] # 사본 만들어서 
                next_elements.remove(e) # 현재 요소 제거해서

                prev_elements.append(e)
                dfs(next_elements) # 다시 호출
                prev_elements.pop()
            
        results = []
        prev_elements =[]
        
        dfs(nums)
        return results