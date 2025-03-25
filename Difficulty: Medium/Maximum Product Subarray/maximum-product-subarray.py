#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		n = len(arr)
        res = float('-inf')
        pref = 1
        suf = 1
        for i in range(len(arr)):
            if pref == 0 : pref =1
            if suf ==0 : suf =1
            pref *= arr[i]
            suf *= arr[n-i-1]
            res = max(res,max(pref,suf))
        return res
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends