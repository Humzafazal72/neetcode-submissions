class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_dict = {}
        for i,num in enumerate(nums):
            nums_dict[num] = i
        seq = {}

        for num in nums:
            if num-1 not in nums_dict.keys():
                seq[num] = 1
            
        for key in seq.keys():
            updated = key
            while(updated+1 in nums_dict):
                seq[key]+=1
                updated=updated+1
        
        if not seq:
            return 0
        
        return max(list(seq.values()))
        

        
        