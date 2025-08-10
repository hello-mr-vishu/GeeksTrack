class Solution:
    def isSubsetSum (self, arr, totalsum):
        def recsum(ind,target):
            if target==0:
                return True
            if ind == 0:
                return arr[ind]==target
            if dp[ind][target]!=-1:
                return dp[ind][target]
            nottaken = recsum(ind-1,target)
            taken = False
            if arr[ind]<=target:
                taken = recsum(ind-1,target-arr[ind])
            dp[ind][target] = taken or nottaken
            return dp[ind][target]
        
        dp = [[-1 for _ in range(totalsum+1)]for _ in range(len(arr)+1)]
        return recsum(len(arr)-1,totalsum)
        