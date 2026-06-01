class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        output = []
        for i,num in enumerate(nums_sorted):
            if i==len(nums_sorted)-1:
                break
            
            if i!=0 and num==nums_sorted[i-1]:
                continue

            s = i+1
            e = len(nums_sorted)-1
            while(s<e):
                sum_ = nums_sorted[s]+nums_sorted[e]
                if sum_+num==0:
                    output.append([num,nums_sorted[s],nums_sorted[e]])
                    s+=1
                    while nums_sorted[s]==nums_sorted[s-1] and s<e:
                        s+=1
                elif sum_+num>0:
                    e-=1
                else:
                    s+=1
        

        return output