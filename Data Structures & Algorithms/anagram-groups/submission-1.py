
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        output = []

        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch)-ord('a')] += 1
            if tuple(count) in res:
                res[tuple(count)].append(s)
            else:
                res[tuple(count)] = [s]
            
        for key, value in res.items():
            output.append(value)
        return output

