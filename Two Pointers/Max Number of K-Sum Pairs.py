class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        p1 = 0
        p2 = len(nums) -1
        ans = 0 
        while p1 < p2 :
            if nums[p1] + nums[p2] > k: 
                p2 = p2 - 1 
            elif nums[p1] + nums[p2] < k: 
                p1 = p1 + 1       
            else :
                p2 = p2 - 1 
                p1 = p1 + 1 
                ans = ans + 1
        return ans
