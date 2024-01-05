class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # 문자의 인덱스를 저장하는 딕셔너리
        max_length = 0
        start = 0

        for end, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1  # 중복된 문자의 인덱스보다 한 칸 뒤부터 시작

            char_index[char] = end  # 문자의 인덱스를 저장
            max_length = max(max_length, end - start + 1)  # 최대 부분 문자열의 길이 갱신

        return max_length