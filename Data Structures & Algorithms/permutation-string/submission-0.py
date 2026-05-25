class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        window = len(s1)
        for c in s1:
            if c in count:
                count[c] +=1
            else:
                count[c] = 1
        print(count)

        for r in range(len(s2)):
            l = r + window
            s = s2[r:l]
            new_count = {}
            for c in s:
                if c in new_count:
                    new_count[c] +=1
                else:
                    new_count[c] = 1
            if new_count == count:
                return True

        return False
            