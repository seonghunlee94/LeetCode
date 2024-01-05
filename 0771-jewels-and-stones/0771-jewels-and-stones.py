class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        char_dict = {char: 0 for char in jewels}
        count = 0
        
        for stone in stones:
            if stone in char_dict:
                count += 1
                
        return count
                