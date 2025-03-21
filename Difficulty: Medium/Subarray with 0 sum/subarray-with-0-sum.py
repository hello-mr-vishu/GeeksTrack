#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr):
        hashset = set()
        s=0
        for i in range(len(arr)):
            s+=arr[i]
            if s in hashset or s==0:
                return True
            hashset.add(s)
            # print(hashset)
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]
        if (Solution().subArrayExists(arr)):
            print("true")
        else:
            print("false")

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends