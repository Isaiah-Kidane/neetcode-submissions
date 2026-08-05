class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = math.ceil(len(nums)/2)
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
            if counts[n] >= maj:
                return n
        #return max(counts.values())