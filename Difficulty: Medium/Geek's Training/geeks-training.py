#User function Template for python3

class Solution:
    def maximumPoints(self, arr):
        n = len(arr)
        dp = [[-1 for _ in range(4)] for _ in range(n)]
        def fun(day,last):
            if dp[day][last]!=-1:
                return dp[day][last]
            if day==0:
                maximum_points = 0
                for task in range(3):
                    if task != last:
                        maximum_points = max(maximum_points,arr[0][task])
                dp[day][last] = maximum_points
                return maximum_points
            maximum_points = 0
            

            
            for task in range(3):
                if task != last:
                    points = arr[day][task]+fun(day-1,task)
                    maximum_points = max(maximum_points,points)
            
            dp[day][last] = maximum_points
                    
            return maximum_points
        
        
        return fun(n-1,3) # 3 means no previous task