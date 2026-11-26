class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        og = []
        rev = []

        for i in str(x):
            og.append(i)

        for i in range(len(og)):
            rev.append(og[len(og)-i-1])

        if og == rev :
            return True

        else :
            return False        
                