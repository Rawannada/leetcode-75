class Solution(object):
    def moveZeroes(self, nums):
        f = 0
        for num in range(len(nums)) :
            if nums[num] != 0:
                nums[f] = nums[num]
                f = f + 1
        
        for num in range (f , len(nums)) :
            nums[num] = 0





        
        