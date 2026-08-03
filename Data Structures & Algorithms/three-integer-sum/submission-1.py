class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num = sorted(nums)
        solve = []
        i = 0
        while i < len(num) - 2  and num[i] <= 0:
            l = i + 1
            r = len(num) - 1
            target = -(num[i])
            while l < r:
                if num[l] + num[r] > target:
                    r -= 1
                elif num[l] + num[r] < target:
                    l += 1
                else:
                    if [num[i],num[l],num[r]] not in solve:
                        solve.append([num[i],num[l],num[r]])
                    l += 1
                    r -= 1


            i += 1
        return solve