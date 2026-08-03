class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        mini = nums[r]

        while l <= r:
            if nums[l] < nums[r]:
                mini = min(mini,nums[l])
                break

            mid = (l+r) // 2
            if nums[mid] >= nums[l]:
                l = mid + 1
                mini = min(mini,nums[mid])
            else:
                r = mid -1
                mini = min(mini,nums[mid])
            
        return mini