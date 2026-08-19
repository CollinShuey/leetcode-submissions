from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        collection = defaultdict(list)

        for s in strs:
            m = [0] * 26
            for c in s:
                m[ord(c)-ord("a")] += 1
            collection[tuple(m)].append(s)

        return list(collection.values())