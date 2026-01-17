class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeroes = nums.count (0)
        ans = [0] * n
        x = 1
        for n in range(len(nums)):
            if nums[n] == 0 :
                index_zero = n
                continue
            x = x * nums[n]
        if zeroes == 0:
            ans =[x // nums[n] for n in  range(len(nums))]  
        elif zeroes == 1:
            ans[index_zero] = x
        return ans



