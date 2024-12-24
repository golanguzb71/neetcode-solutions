from types import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
	l =r =0
	while r<n:
	    nums[l]=nums[r]
	    while r <n and nums[r] == nums[l]:
		r+=1
	    l+=1		
	return l	