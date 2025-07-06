#User function Template for python3
class Solution:
	
	def findMaxSum(self,arr):
		def fun(dp ,ind):
		    if ind == 0:
		        return arr[ind]
		    if ind<0:
		        return 0
		    if dp[ind]!= -1:
		        return dp[ind]
		        
		    pick = arr[ind]+ fun(dp,ind-2)
		    notpick = 0 + fun(dp,ind-1)
		    
		    dp[ind] = max(pick , notpick)
		    return dp[ind]
		dp = [-1]*(len(arr)+1)
		return fun(dp,len(arr)-1)