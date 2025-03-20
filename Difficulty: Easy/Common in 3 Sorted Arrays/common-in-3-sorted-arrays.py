#User function Template for python3

class Solution:
    def commonElements(self, arr1, arr2, arr3):
        if not arr1 or not arr2 or not arr3:
            return -1
        lst = []
        hs = {}
        for i in arr1:
            hs[i]=1
        # print(hs)
        for i in arr2:
            if i in hs and hs[i]==1:
                hs[i]=2

        # print(hs)
        for i in arr3:
            if i in hs and hs[i]==2:
                hs[i]=3


        # print(hs)
        for k,cnt in sorted(hs.items()):
            if cnt == 3:
                lst.append(k)
        
        # print(lst)/
        return lst

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        brr = list(map(int, input().split()))
        crr = list(map(int, input().split()))
        ob = Solution()
        res = ob.commonElements(arr, brr, crr)
        if len(res) == 0:
            print(-1)
        else:
            print(" ".join(map(str, res)))
        print("~")
# } Driver Code Ends