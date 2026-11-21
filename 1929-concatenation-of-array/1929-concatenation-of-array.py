class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        
        temp = []
        temp = nums

        for i in range(len(nums)):
            nums.append(temp[i])

        return nums    