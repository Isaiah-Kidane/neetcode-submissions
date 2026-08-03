class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ana1 = {}
        ana2 = {}

        if len(s) != len(t):
            return False

        for i in s:
            if i not in ana1:
                ana1[i] = 1
            else:
                ana1[i] += 1
        
        for i in t:
            if i not in ana2:
                ana2[i] = 1
            else:
                ana2[i] += 1
        
        if ana1 != ana2:
            return False
        else:
            return True