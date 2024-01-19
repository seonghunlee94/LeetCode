class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # 입력이 빈 문자열인 경우
        if not digits:  
            return []   

        # 각 숫자에 매핑된 문자들
        keypad = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # 숫자 조합으로 만들 수 있는 문자의 조합(재귀 함수).
        def num_backtrack_combined_char(index, path):
            
            if index == len(digits):
                combined_char.append(path)
                return
            
            current_digit = digits[index]
            for char in keypad[current_digit]:
                num_backtrack_combined_char(index + 1, path + char)
                
            

        combined_char = []
        num_backtrack_combined_char(0, "")
        return combined_char
        
        

                
                
                
                
        