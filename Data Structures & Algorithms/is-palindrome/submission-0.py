class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = "".join(ch for ch in s if ch.isalnum())
        i = 0
        j = len(new_s)-1
        while j > i:
            if new_s[i] != new_s[j]:
                return False
            i +=1
            j -=1

        return True