class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for i in strs:
            length = len(i)
            encode += f"{length}#{i}"
        return encode

    def decode(self, s: str) -> List[str]:
        decode = []
        i = 0
        while i < len(s):
            j = s.index("#",i)
            length = int(s[i:j])
            decode.append(s[j+1:j+1+length])
            i = j + 1 + length
        return decode
                
