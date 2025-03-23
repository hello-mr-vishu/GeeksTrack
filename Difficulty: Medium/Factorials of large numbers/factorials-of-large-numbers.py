#User function Template for python3

class Solution:
    def factorial(self, n):
        if n==0 or n==1:
            return [1]
    
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        # print(s)
        return [int(digit) for digit in str(fact)]  

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorial(N)
        print(" ".join(
            str(i) for i in
            ans))  # Join each digit to form the full number without spaces
        print("~")

# } Driver Code Ends