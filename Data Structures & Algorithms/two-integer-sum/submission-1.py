class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i,v in enumerate(nums):
            pair = target - v
            if pair in prevMap:
                return[prevMap[pair], i]
            prevMap[v] = i

        
        
        # length = len(nums)
        # index = []
        # for i in range(length):
        #     for j in range(length):
        #         if nums[i] != nums[j] and nums[i]+nums[j]==target:
        #             index.append(i)
        #             index.append(j)
        #             return index
                    #return (nums[i],nums[j])