class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for n in strs:
                group[tuple(sorted(n))].append(n)
        print(group.values())
        return list(group.values())