class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        row_strengths = {}
        count = 0
        
        for i in range(len(mat)):
            count = mat[i].count(1)
            row_strengths[i] = count
        
        # 딕셔너리를 강도(count)를 기준으로 정렬
        sorted_weaker = sorted(row_strengths.items(), key=lambda x: x[1])

        result = []
        # 튜플 형식일 때 for문에서는 key, value로 받아준다.
        for key, _ in sorted_weaker[:k]:
            result.append(key)
        return result
