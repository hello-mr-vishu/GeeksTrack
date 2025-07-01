#User function Template for python3
class Solution:
    def minCost(self, height):
        # def minCost1(n,height):
        #     if n == 1 or n==0:
        #         return 0
        #     if n==2:
        #         return abs(height[n-1]-height[n-2])
                
        #     return min(minCost1(n-1,height)+abs(height[n-1]-height[n-2]),minCost1(n-2,height)+abs(height[n-1]-height[n-3]))
        # return minCost1(len(height),height)
        
        def minCost2(n,height,dp):
            if n==1:
                return 0
            if n==2:
                return abs(height[n-1]-height[n-2])
            
            if dp[n] != -1:
                return dp[n]
            
            dp[n] = min(minCost2(n-1,height,dp)+abs(height[n-1]-height[n-2]),minCost2(n-2,height,dp)+abs(height[n-1]-height[n-3]))
            return dp[n]
            
        dp = [-1]*(len(height) +1)
        return minCost2(len(height),height,dp)