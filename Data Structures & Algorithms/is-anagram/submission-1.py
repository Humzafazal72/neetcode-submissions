class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_ = {}

        if len(s) != len(t):
           return False     

        for char in s:
            if char not in dict_.keys():
                dict_[char] = 1
            else:
                dict_[char] += 1

        for char in t:
            if char not in dict_.keys() or dict_[char]==0:
                return False
            else:
                dict_[char]-=1 
        
        return True