class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        from collections import Counter

        c = Counter(nums)
        if 0 not in c.keys():        
            product = [math.prod(nums[1:])]
            for idx in range(1,len(nums)):
                product.append(int((product[idx-1]/nums[idx])*nums[idx-1]))
            return product 
        
        if c[0]>1:
            return [0]*len(nums)
        else:
            product = [0]*len(nums)
            idx_0 = nums.index(0)
            if idx_0+1>=len(nums):
                final = len(nums)
            else:
                final = idx_0+1
            product[idx_0] = math.prod(nums[:idx_0]+nums[final:])
            return product



        