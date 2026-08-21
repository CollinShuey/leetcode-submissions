class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        window = {}
        tcounts = {}

        for ch in t:
            tcounts[ch] = 1 + tcounts.get(ch,0)
        
        have, need = 0, len(tcounts)
        res, resLen = [-1,-1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in tcounts and window[c] == tcounts[c]:
                have += 1

            while have == need:
                #update res
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res = [l,r]
                window[s[l]] -= 1
                if s[l] in tcounts and window[s[l]] < tcounts[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r+1] if resLen != float("inf") else ""




        


        