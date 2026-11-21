class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        Shuffle_List = []
        list1 = []
        list2 = []

        for i in range(n):
            list1.append(nums[i])

        for i in range(n,len(nums)):
            list2.append(nums[i])

        for i in range(n):

            Shuffle_List.append(list1[i])
            Shuffle_List.append(list2[i])

        return Shuffle_List    

