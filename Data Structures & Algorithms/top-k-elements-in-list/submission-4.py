from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top = defaultdict(int)
        freq= []

        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return nums

        for i in nums:
            top[i] += 1 
            

        for x in range(k):
            key = max(top, key = top.get)
            # print(key)
            freq.append(key)
            top.pop(key)


        return freq

         