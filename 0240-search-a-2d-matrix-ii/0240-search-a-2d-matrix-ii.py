class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        row = 0
        col = len(matrix[0]) - 1
        
        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1
            
            
        return False
        
        
        
        
        
        
        
        
#         x = y = 0
        
#         for idx in range(len(matrix)):
            
#             # 값이 작으면 인덱스 리턴
#             if matrix[idx][idx] > target:
#                 x = y = idx
#                 break
            
#             # 값이 같으면 True 리턴
#             elif matrix[idx][idx] == target:
#                 return True
            
        
#         # for문으로 (0, 2) ~ (1, 2) (2, 2) 돌리기
#         for i in range(x):
#             if matrix[i][y] == target:
#                 return True
        
#         # for문으로 (2, 0) ~ (2, 1) (2, 2) 돌리기
#         for i in range(y):
#             if matrix[x][i] == target:
#                 return True
        
#         return False