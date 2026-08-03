class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for i in s:
            if i.isalnum():
                string += i
        print(string)
        strin = string.lower()
        print(strin)
        l = 0
        r = len(strin) - 1

        for i in range(int(len(strin)/2)):
            if strin[l] == strin[r]:
                l += 1
                r -= 1
                print(i)
            else:
                return False
        
        return True


