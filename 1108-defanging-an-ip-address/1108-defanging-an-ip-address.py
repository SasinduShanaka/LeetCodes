class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        result = ""
        i = 0
        while i < len(address) :

            if address[i] == ".":
                result += "[" + "." + "]" 
            else :
                result += address[i]

            i += 1 
        return result          