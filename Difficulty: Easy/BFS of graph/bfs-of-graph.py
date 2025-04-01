#User function Template for python3
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        from collections import deque
        v = len(adj)
        res = []
        s = 0
        q = deque()
        visited = [False]*v
        visited[s] = True
        q.append(s)
        while q:
            curr = q.popleft()
            res.append(curr)
            for x in adj[curr]:
                if not visited[x]:
                    visited[x] = True
                    q.append(x)
        return res

#{ 
 # Driver Code Starts
import sys


#Position this line where user code will be pasted.
def main():
    tc = int(sys.stdin.readline().strip())

    for _ in range(tc):
        V = int(sys.stdin.readline().strip())  # Number of vertices
        adj = []  # Adjacency list

        for _ in range(V):
            input_line = sys.stdin.readline().strip()
            node = list(map(int, input_line.split())) if input_line else []
            adj.append(node)

        obj = Solution()
        ans = obj.bfs(adj)
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends