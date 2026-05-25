class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seens = dict()
        seent = dict()
        for ch in s:
            if ch in seens:
                seens[ch] +=1
            else:
                seens[ch] = 1
        for ch in t:
            if ch in seent:
                seent[ch] +=1
            else:
                seent[ch] = 1
        if seens == seent:
            return True
        else:
            return False
        
