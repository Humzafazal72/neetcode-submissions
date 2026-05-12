class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded+=string+"#!)"
        return encoded

    def decode(self, s: str) -> List[str]:
        return s.split("#!)")[:-1]
