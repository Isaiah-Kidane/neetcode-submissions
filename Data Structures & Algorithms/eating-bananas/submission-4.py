class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi = max(piles)
        
        l = 1
        r = maxi
        mini =maxi
        
        while l <= r:
            mid = (l + r) // 2
            total = 0
            for p in piles:
                total += math.ceil(p/mid)

            if total > h:
                l = mid + 1
            else:
                mini = min(mini,mid)
                r = mid - 1
            
        return mini