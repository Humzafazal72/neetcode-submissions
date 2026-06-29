class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = [0]*26
        for char in s1:
            freq[ord(char)-97]+=1

        if len(s2)<len(s1):
            return False

        start,end = 0,len(s1)-1
        
        match = [0]*26
        while end<len(s2):
            # print("match: ",match)
            # print("Freq: ",freq)
            # print(s2[start:end+1])
            if start==0:
                for i in s2[start:end+1]:
                    # print("idx: ",i)
                    match[ord(i)-97]+=1
            else:
                match[ord(s2[start-1])-97]-=1
                match[ord(s2[end])-97]+=1
            
            if match == freq:
                return True
            
            start+=1
            end+=1
        
        return False
