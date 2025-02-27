#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        ht = {}
        cnt=0
        i=0
        j=0
        while i<len(a) or j<len(b):
            if i<len(a) and a[i]not in ht:
                ht[a[i]]=1
                cnt+=1
            if j<len(b) and b[j]not in ht:
                ht[b[j]] =1
                cnt+=1
            i+=1
            j+=1
        return cnt
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()

        print(ob.findUnion(a, b))
        print("~")

# } Driver Code Ends