class Solution:
    def minWindow(self, s: str, t: str) -> str:
        

        
        l = r = 0
        tcounts = {}
        currWindow = {}
        res , resLen = [-1,-1], float('inf')
        for ch in t:
            tcounts[ch] = 1 + tcounts.get(ch,0)
            currWindow[ch] = 0
        have = 0
        need = len(tcounts.keys())

        for r in range(len(s)):

            if s[r] in currWindow:
                currWindow[s[r]] += 1
                if currWindow[s[r]] == tcounts[s[r]]:
                    have += 1
            else:
                continue
            
            while have == need:
                if resLen > (r-l+1):
                    res = [l,r]
                    resLen = r-l+1
                if s[l] in tcounts:
                    currWindow[s[l]] -= 1
                if s[l] in tcounts and currWindow[s[l]] < tcounts[s[l]]:
                    have -= 1
                l += 1

        l,r = res
        return s[l:r+1]