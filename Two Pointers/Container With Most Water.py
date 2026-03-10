class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        max_amount = 0

        for i in range(len(height)):
            amount = min(height[l],height[r]) * (r - l)
            max_amount = max(amount ,max_amount)

            if height[l] >height[r] :
                r = r - 1
            else :
                l = l + 1
        return max_amount   