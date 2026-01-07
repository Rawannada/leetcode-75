class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ans=0
        flowerbed.insert(0,0)
        flowerbed.append(0)
        for i in range (1,len(flowerbed)-1):
            if flowerbed[i]==flowerbed[i-1]==flowerbed[i+1] == 0:
                flowerbed[i]=1
                ans = ans+1
        return ans >= n
            