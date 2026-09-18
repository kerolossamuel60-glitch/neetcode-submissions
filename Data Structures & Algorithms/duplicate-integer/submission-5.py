class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        left=0
        right=1
        while left <=len(nums)-2:
            if nums[left]==nums[right]:
                return True
            else:
                left+=1
                right+=1
        return False 
        