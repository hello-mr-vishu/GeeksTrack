#User function Template for python3

class Solution:
    def maximumPoints(self, arr):
        n = len(arr)
        prev = [0]*4
        
        # Base case: day 0
        prev[0] = max(arr[0][1], arr[0][2])  # Last was 0 → skip 0
        prev[1] = max(arr[0][0], arr[0][2])  # Last was 1 → skip 1
        prev[2] = max(arr[0][0], arr[0][1])  # Last was 2 → skip 2
        prev[3] = max(arr[0])                # No restriction
        
        for day in range(1, n):
            curr = [0] * 4
            for last in range(4):
                max_points = 0
                for task in range(3):
                    if task != last:
                        points = arr[day][task] + prev[task]
                        max_points = max(max_points, points)
                curr[last] = max_points
            prev = curr  # Move to next day

        return prev[3]
        
        # Tabulation
        # dp = [[-1 for _ in range(4)] for _ in range(n)]
        
        
        # dp[0][0] = max(arr[0][1], arr[0][2])  # Last task was 0 → skip 0
        # dp[0][1] = max(arr[0][0], arr[0][2])  # Last task was 1 → skip 1
        # dp[0][2] = max(arr[0][0], arr[0][1])  # Last task was 2 → skip 2
        # dp[0][3] = max(arr[0][0], arr[0][1], arr[0][2])  # No last task → pick best
        
        # for day in range(1,n):
        #     for last in range(4):
        #         dp[day][last] = 0
        #         for task in range(3):
                   
        #             if  task != last:
        #                 points = arr[day][task] + dp[day-1][task]
        #                 dp[day][last]= max(dp[day][last],points)
                
        # return dp[n-1][3]
        
 
        
        
        
        
        
        
        # Memoization
        
        # def fun(day,last):
        #     if dp[day][last]!=-1:
        #         return dp[day][last]
        #     if day==0:
        #         maximum_points = 0
        #         for task in range(3):
        #             if task != last:
        #                 maximum_points = max(maximum_points,arr[0][task])
        #         dp[day][last] = maximum_points
        #         return maximum_points
        #     maximum_points = 0
            

            
        #     for task in range(3):
        #         if task != last:
        #             points = arr[day][task]+fun(day-1,task)
        #             maximum_points = max(maximum_points,points)
            
        #     dp[day][last] = maximum_points
                    
        #     return maximum_points
        
        
        # return fun(n-1,3) # 3 means no previous task