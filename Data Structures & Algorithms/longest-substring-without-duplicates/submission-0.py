class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        start,end = 0,1
        dict_ = {s[start]:0}
        max_len  = 1

        while end<len(s):
            print(s[end], dict_)
            if s[end] in dict_:
                idx = dict_[s[end]]
                for i in range(start,idx+1):
                    del dict_[s[i]]
                start = idx+1
            else:
                dict_[s[end]] = end
                end+=1
            
            max_len = max(max_len,end-start)
            
        return max_len