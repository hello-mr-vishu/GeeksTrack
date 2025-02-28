class Solution:
    def maxSubArraySum(self, arr):
        # Your code here
        cursum = 0
        maxsum = float('-inf')
        for i in range(len(arr)):
            cursum +=arr[i]
            maxsum = max(maxsum,cursum)
            if cursum <0:
                cursum = 0
        return maxsum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends