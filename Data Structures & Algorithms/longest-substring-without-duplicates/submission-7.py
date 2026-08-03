class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0


        l = 0
        r = 0
        maxi = 1
        curr = ""
        while r < len(s):
            if s[r] not in curr:
                curr += s[r]
                r += 1
                maxi = max(maxi,len(curr))
            else:
                curr = curr[1:]
                l += 1

        return maxi

                
                

