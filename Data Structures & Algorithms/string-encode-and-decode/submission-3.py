class Solution:


    def encode(self, strs: List[str]) -> str:
        output=""
        count = [0]*len(strs)
        for i in strs:
            output += i+"£"
        return output


    def decode(self, s: str) -> List[str]:
        return s.split("£")[:-1]
        