class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i,n in enumerate(nums):
            pair = target - n
            if pair in sums:
                return [sums[pair],i]
            sums[n] = i