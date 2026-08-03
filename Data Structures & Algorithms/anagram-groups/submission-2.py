class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        for i, s in enumerate(strs):
            ssort = tuple(sorted(s))
            ana[ssort].append(s) 
        return list(ana.values())
        
        # ana = {}
        # for i, s in enumerate(strs):
        #     ssort = sorted(s)
        #     if tuple(ssort) not in ana:
        #         ana[tuple(ssort)] = s
        #     else:
        #         ana[tuple(ssort)] += s
        # return ana