class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        num = 0
        for i in range(len(stones)):
            if stones[i] in jewels:
               num += 1 
        return num