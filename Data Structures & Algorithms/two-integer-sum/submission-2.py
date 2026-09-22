class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i , l in enumerate(nums):
            t=target-l
            if t in seen:
                 return[seen[t],i]
            seen[l]=i