class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = set()

        for i in nums:
            if i not in table:
                table.add(i)
            else:
                return True
            

        return False