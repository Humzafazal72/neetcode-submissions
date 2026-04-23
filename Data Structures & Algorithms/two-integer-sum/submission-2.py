class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}
        for idx,num in enumerate(nums):
            if not dict_:
                dict_[num] = idx
                continue
            
            diff  = target-num
            if diff in dict_.keys():
                return [dict_[diff],idx]
            else:
                dict_[num]=idx
        
        return []
        