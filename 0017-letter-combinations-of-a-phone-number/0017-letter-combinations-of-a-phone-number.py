class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:  # 입력이 빈 문자열인 경우
            return []   # 빈 리스트 반환

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

        # 재귀적으로 문자 조합을 찾는 함수
        def backtrack(index, path):
            if index == len(digits):  # 현재 탐색 인덱스가 입력의 길이와 같으면
                combinations.append(path)  # 조합 리스트에 결과 추가
                return

            current_digit = digits[index]  # 현재 숫자
            for char in keypad[current_digit]:  # 현재 숫자에 해당하는 문자들에 대해 반복
                backtrack(index + 1, path + char)  # 다음 숫자 조합을 찾기 위해 재귀 호출

        combinations = []  # 모든 조합을 담을 리스트
        backtrack(0, "")   # 재귀 함수 호출 시작
        return combinations  # 모든 조합 반환
                

                
                
                
                
        