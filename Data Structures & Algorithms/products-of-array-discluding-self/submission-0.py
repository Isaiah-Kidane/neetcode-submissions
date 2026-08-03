class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        solution = []
        prentry = 1
        postentry = 1

        for i in nums:
            prentry *= i
            prefix.append(prentry)
        
        for i in reversed(nums):
            postentry *= i
            postfix.append(postentry)

        revpostfix = list(reversed(postfix))
        print(prefix)
        print(postfix)
        for i in range( len(nums)):
            if i == 0:
                solution.append(revpostfix[i+1])
            elif i == (len(nums))-1:
                solution.append(prefix[i-1])
            else:    
                solution.append(prefix[i-1] * revpostfix[i+1])

        return solution
