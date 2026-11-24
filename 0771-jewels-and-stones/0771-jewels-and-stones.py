class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        count = 0
        i = 0
        

        while i < len(stones):
            j = 0
            while j <len(jewels):
               if jewels[j] == stones[i]:
                 count += 1
                 break
               j += 1

            i += 1

        return count        