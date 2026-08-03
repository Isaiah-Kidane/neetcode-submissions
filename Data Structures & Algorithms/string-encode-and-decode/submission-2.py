class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for i in range(len(strs)):
            length = len(strs[i])
            encoded += str(length) + "$" + strs[i]
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "$":
                j+=1
            length = int(s[i:j])
            decoded.append(s[j+1:j+length+1])
            i = 1+length+j
            print(i)
            print(j)
        return decoded
                
