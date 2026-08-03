class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = set()
        for i in nums:
            if i not in dupe:
                dupe.add(i)
            else:
                return True
        return False
