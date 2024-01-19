class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # 숫자를 받아 순열을 만들어주는 함수(dfs)
        def num_dfs_permutations(elements):
            
            if len(elements) == 0:
                permutations_list.append(prev_elements_list[:])
             
            # 요소 하나씩 옮겨 넣는 작업
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                
                prev_elements_list.append(e)
                num_dfs_permutations(next_elements)
                prev_elements_list.pop()
            
            
        
        prev_elements_list = []
        permutations_list = []
        
        num_dfs_permutations(nums)
        
        return permutations_list