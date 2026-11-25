class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        counter = {}
        result = 0

        for w in s :
            counter[w] = counter.get(w,0) + 1
        
        for c in counter :
            if counter[c] == 1:
                result = c
                break
 

        for i in range(len(s)):
            if s[i] == result :
                return i
        
        if result == 0:
          return -1
