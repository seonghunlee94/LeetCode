class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # 조합 만드는 함수
        def combine_dfs(elements, start, k):    
            if k == 0:
                combinations_list.append(elements[:])
                return

            for i in range(start, n+1):
                elements.append(i)
                combine_dfs(elements, i+1, k-1) 
                elements.pop()


        combinations_list = []
        combine_dfs([], 1, k)
        return combinations_list

    
