class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clean = ""
        i = 0
        while i < len(s):

            if s[i].isalnum():
                clean += s[i]
            i += 1
        
        reverse = clean[::-1]
        print(clean)
        print(reverse)
        return clean == reverse


        x = 0
        y = -1
        while clean[x] == clean[y]:
            x += 1
            y -= 1
            if x == (len(s)/2) +2 :
                return True
        return False        


        