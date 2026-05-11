class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        hash = defaultdict(list)
        
        for str_ in strs:
            key = [0]*26
            for s in str_:
                idx = ord(s)%97
                key[idx] += 1
                
            hash.setdefault(tuple(key),[]).append(str_)
        
        output = []
        for values in hash.values():
            output.append(values)
        
        return output
        