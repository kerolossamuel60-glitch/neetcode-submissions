class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        max_array=0
        while left<right:
            if heights[left]<=heights[right]:
                array=heights[left]*(right-left)
                if array>max_array:
                    max_array=array
                left+=1
            else:
                array=heights[right]*(right-left)
                if array>max_array:
                    max_array=array
                right-=1
        return max_array 

        