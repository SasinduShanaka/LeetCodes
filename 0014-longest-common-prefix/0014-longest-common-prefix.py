class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        if not strs:
            return ""
        
        
        for i in range(len(strs[0])):
            char = strs[0][i]
            
           
            for j in range(1, len(strs)):
                
                
                if i == len(strs[j]) or strs[j][i] != char:
                    
                    return strs[0][:i]
                    
        # If the outer loop finishes without returning, the whole first word is the prefix
        return strs[0]