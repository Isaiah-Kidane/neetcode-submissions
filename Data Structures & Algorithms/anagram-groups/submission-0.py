from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anMap = defaultdict(list)
        for i,s in enumerate(strs):
            s_sorted = tuple(sorted(s))
            anMap[s_sorted].append(s)
        return list(anMap.values())

