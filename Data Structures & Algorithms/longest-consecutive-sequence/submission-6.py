class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num = set()

        for n in nums:
            num.add(n)

        long = 1
        cur = 1
        for i in range(len(nums)):
            cur = 1
            val = nums[i]
            if (val-1) not in num:

                while (val + 1) in num:
                    cur += 1
                    val += 1
            long = max(long, cur)
                
        return long