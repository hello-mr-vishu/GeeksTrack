
class Solution:
    def countAndMerge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        left = arr[l:m+1]
        right = arr[m+1:r+1]

        res = 0
        i, j, k = 0, 0, l 

        while i < n1 and j < n2:
            if left[i] <= right[j]:  
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                res += (n1 - i) 
            k += 1 
        while i < n1:
            arr[k] = left[i]
            i += 1
            k += 1 

        while j < n2:
            arr[k] = right[j]
            j += 1
            k += 1 

        return res

 
    def countInv(self, arr, l, r):
        res = 0
        if l < r:
            m = (l + r) // 2
            res += self.countInv(arr, l, m)
            res += self.countInv(arr, m + 1, r)
            res += self.countAndMerge(arr, l, m, r)
        return res

    def inversionCount(self, arr):
        return self.countInv(arr, 0, len(arr) - 1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a))
        print("~")

# } Driver Code Ends