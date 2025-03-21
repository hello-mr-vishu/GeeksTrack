#User function Template for python3

class Solution:
    def rearrange(self,arr):
        # i = 0
        # j = 0
        # while i<len(arr) and j <len(arr):
        #     while arr[j]>0:
        #         j+=1
        #         break
        #     if i%2==0 and arr[i]<0:
        #         temp = arr[i]
        #         arr[i] = arr[j]
        #         arr[j] = temp
        #     if i%2!=0 and arr[i]>0:
        #         temp = arr[i]
        #         arr[i]= arr[j]
        #         arr[j] = temp
        #     i+=1   
        #     j+=1
        # return arr
        
        pos = []
        neg = []
        for i in arr:
            if i>=0:
                pos.append(i)
            else:
                neg.append(i)
                
        i = 0
        posindx,negindx=0,0
        while posindx<len(pos) and negindx<len(neg):
            if i%2==0:
                arr[i] = pos[posindx]
                posindx+=1
            else:
                arr[i] =neg[negindx]
                negindx+=1
            i+=1
            
        while posindx<len(pos):
            arr[i] = pos[posindx]
            posindx+=1
            i+=1
        while negindx<len(neg):
            arr[i] = neg[negindx]
            negindx+=1
            i+=1
            
        return arr
        
        
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends