class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_ = {}
        for num in nums:
            if num in dict_.keys():
                return True
            else:
                dict_[num] = num
        return False