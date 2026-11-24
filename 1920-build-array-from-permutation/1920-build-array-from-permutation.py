class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        
         temp = []

         for i in range(len(nums)):
            temp.append(nums[nums[i]])

         return temp  
          