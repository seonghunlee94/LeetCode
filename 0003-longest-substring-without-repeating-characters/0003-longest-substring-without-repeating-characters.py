class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 반복되는 문자열이 가장 긴 텍스트 리턴
        # 투포인트 - index와 start 변수로 비교
        # 비교하기 위해서 hash table 생성 - used = {}
        # 최대값 maxlangth 변수 생성
        
        # for index, char in enumerate(s) 
        
        
        # 1. 투 포인트로 같은 문자가 들어 왔는지 확인.
        # used 있으면 - 반복되는 문자. used[char] = start + 1
        # used 없으면 - 새로운 문자. 
        # 최대값 갱신 = max(maxlength, index - start + 1 )

        
        # 최신화 used[char] = index

        used = {}
        maxlength = start = 0
        
        for index, char in enumerate(s):
            # 해시테이블은 in으로 조회
            if char in used and used[char] >= start:
                start = used[char] + 1
            else:
                maxlength = max(maxlength, index - start + 1)
                
                
            used[char] = index
            
        return maxlength