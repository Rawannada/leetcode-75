class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_arr = sum(nums[:k])
        max_avg = sum_arr/k
        for n in range(k,len(nums)) :
            sum_arr = sum_arr -nums[n-k] + nums[n]
            avg = sum_arr / k
            max_avg = max(avg ,max_avg)
        return max_avg
