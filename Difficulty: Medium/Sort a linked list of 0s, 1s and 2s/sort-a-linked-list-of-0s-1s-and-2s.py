#User function Template for python3
'''
	Your task is to segregate the list of 
	0s,1s and 2s.
	
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here
        count0 =0
        count1 = 0
        count2 =0
        curr = head
        while curr:
            if curr.data == 0:
                count0+=1
            elif curr.data == 1:
                count1 +=1
            else:
                count2 +=1
            curr = curr.next
        curr = head
        while curr:
            if count0>0:
                curr.data =0
                count0-=1
            elif count1>0:
                curr.data=1
                count1-=1
            else:
                curr.data=2
                count2-=1
            curr = curr.next
        return head
        # curr = head
        # print(curr.data+"->")
        # curr =curr.next
        # while curr:
        #     print(curr.data)
        #     curr = curr.next
        


#{ 
 # Driver Code Starts
# Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for value in arr[1:]:
                tail.next = Node(value)
                tail = tail.next

        printList(Solution().segregate(head))
        print("~")

# } Driver Code Ends