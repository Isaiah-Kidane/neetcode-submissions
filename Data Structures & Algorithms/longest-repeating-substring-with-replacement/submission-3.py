class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        map = {s[0]:0}
        l = 0
        #r = 1
        maxi = 0

        for i in range(len(s)):
        #while l < len(s):
            if s[i] not in map:
                map[s[i]] = 1
            else:
                map[s[i]] += 1
            
            sublen = (i-l ) +1

            if sublen - max(map.values()) <= k:
                maxi = max(maxi,sublen)
            else:
                map[s[l]] -= 1
                l += 1
        return maxi
            

            



