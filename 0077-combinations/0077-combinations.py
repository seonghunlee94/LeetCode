class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # 시작점, 
        def dfs(elements, start, k):    
            if k == 0:
                result.append(elements[:])
                return

            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()


        result = []
        dfs([], 1, k)
        return result
