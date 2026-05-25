class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_s = ""
        for s in strs:
            l = str(len(s))
            encode_s +=l
            encode_s +="#"
            encode_s +=s
        print(encode_s)
        return encode_s
        
    def decode(self, s: str) -> List[str]:
        decode_s=[]
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j +=1
            length = int(s[i:j])
            i = j+1
            j = i+length
            decode_s.append(s[i:j])
            i = j
        return decode_s