class Solution:
    def isValid(self, s: str) -> bool:

        hashMap = {")":"(","}":"{","]":"["}

        stack = []

        for ch in s:
            if ch not in hashMap:
                stack.append(ch)
            else:
                if not stack:
                    return False
                opening = stack.pop()
                if opening != hashMap[ch]:
                    return False
        

        return not stack


        