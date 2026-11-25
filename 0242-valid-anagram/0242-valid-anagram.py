class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         
         seen1 = {}
         seen2 = {}

         for c in s :
            if c in seen1:
                seen1[c] += 1
            else:
                seen1[c] = 1 

         for w in t :
            if w in seen2:
                seen2[w] += 1
            else:
                seen2[w] = 1  
                   
         return seen1 == seen2