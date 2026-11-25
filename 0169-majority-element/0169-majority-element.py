class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        count = {}

        for num in nums:
            count[num] = count.get(num,0) + 1

        result = max(count,key = count.get)

        return result