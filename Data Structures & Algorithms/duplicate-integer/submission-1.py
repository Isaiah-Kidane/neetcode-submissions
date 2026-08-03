class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsort = sorted(nums)
        length = len(nums)-1
        for i in range(length):
            if numsort[i]==numsort[i+1]:
                return True

        return False