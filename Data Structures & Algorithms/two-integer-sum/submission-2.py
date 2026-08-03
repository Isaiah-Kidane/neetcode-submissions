class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twosum = {}
        for i,n in enumerate(nums):
            pair = target - n
            if pair in twosum:
                return [twosum[pair],i]
            twosum[n] = i
        return []

            