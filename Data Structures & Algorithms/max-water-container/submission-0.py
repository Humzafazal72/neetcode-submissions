class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_ = 0
        start = 0
        end = len(heights)-1

        while start<end:
            width = end - start
            
            if heights[start] < heights[end]:
                height = heights[start]
                start+=1
            else:
                height = heights[end]
                end-=1

            area = height*width

            max_ = max_ if area < max_ else area

        return max_        