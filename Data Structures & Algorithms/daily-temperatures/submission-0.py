class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] *len(temperatures)
        stack = []
        x = 0

        for i,n in enumerate(temperatures):
            while stack and n > stack[-1][0]:
                stackT, stackInd = stack.pop()
                out[stackInd] = (i-stackInd)
            stack.append([n,i])
        return out