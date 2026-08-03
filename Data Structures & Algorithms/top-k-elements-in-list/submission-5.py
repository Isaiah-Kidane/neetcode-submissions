class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top = defaultdict(int)
        
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return nums
        
        for i in nums:
            top[i]+= 1
            
        ret = []
        for i in range(k):
            maxi = max(top, key = top.get)
            ret.append(maxi)
            top.pop(maxi)
        return ret