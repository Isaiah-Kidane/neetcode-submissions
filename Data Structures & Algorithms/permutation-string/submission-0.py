class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        str1 = [0]*26
        str2 = [0]*26

        r = len(s1) - 1
        for i in range(len(s1)):
            str1[(ord(s1[i]) - ord("a"))] += 1
        
        for i in range(len(s1)):
            str2[(ord(s2[i]) - ord("a"))] += 1
        
        for i in range(len(s2) - len(s1) + 1):
            if i != 0:
                str2[(ord(s2[r]) - ord("a"))] += 1
            if str1 == str2:
                return True
            
            str2[(ord(s2[i]) - ord("a"))] -= 1
            r += 1
        return False
        
