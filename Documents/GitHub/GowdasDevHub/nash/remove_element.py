class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    	# initializing the variable in order to track non-value element
        j = 0

        for i in range(len(nums)):

        	if nums[i] != val:
        		# moving the non-value element to the jth position
        		nums[j] = nums[i]
        		# incrementing the j to the next position
        		j += 1

        return j
