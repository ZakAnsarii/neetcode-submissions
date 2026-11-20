class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS,countT = {},{}

        if len(s) != len(t):
            return False

        for ch in range(len(s)):
            countS[s[ch]] = countS.get(s[ch],0) + 1
            countT[t[ch]] = countT.get(t[ch], 0) + 1
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True