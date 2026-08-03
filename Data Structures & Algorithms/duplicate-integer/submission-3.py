class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = []

        for i in nums:
            if i not in table:
                table.append(i)
            else:
                return True
            

        return False