#{ 
 # Driver Code Starts

# } Driver Code Ends
class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        cnt0 =0
        cnt1 =0
        cnt2 =0
        for i in range(len(arr)):
            if arr[i]==0:
                cnt0+=1
            elif arr[i]==1:
                cnt1+=1
            else:
                cnt2+=1
            
        for j in range(cnt0):
            arr[j] = 0
        for j in range(cnt0,cnt1+cnt0):
            arr[j] = 1
        for j in range(cnt1+cnt0,cnt0+cnt1+cnt2):
            arr[j] = 2
        return arr
#{ 
 # Driver Code Starts.
def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split())
                   )  # Read the array as space-separated integers
        ob.sort012(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array
        print("~")
        
if __name__ == "__main__":
    main()

# } Driver Code Ends