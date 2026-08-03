class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {}
        for i,m in enumerate(nums):
            pair = target - m
            if pair in n:
                return [n[pair],i]
            n[m] = i

        # for i in nums:
        #     pair = target - i
        #     if pair in n:
        #         return [nums[i],nums[pair]]