class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        l = 0
        maxCount = 0

        for ch in s:
            if ch in seen:
                while ch in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(ch)


            else:
                seen.add(ch)
                maxCount = max(maxCount,len(seen))

        return maxCount



    
        