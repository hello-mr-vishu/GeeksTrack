from collections import deque

class Solution:
	def isCycle(self, V, edges):
		visited = [False] * V
# 		print(V)
# 		print(edges)
		n = V
		m = len(edges[0])
		adj = [[]for _ in range(V)]
		
		for u , v in edges:
		    adj[u].append(v)
		    adj[v].append(u)
		q = deque()
		def bfs(start):
		    q.append((start,-1))
		    visited[start] = True
		    while q:
		        node , parent = q.popleft()
		        for neighbour in adj[node]:
		            if not visited[neighbour]:
    		            visited[neighbour] = True
    		            q.append((neighbour,node))
		            elif neighbour != parent:
		                return True
		    return False
		
		for i in range(n):
		    if not visited[i]:
		        if bfs(i):
		            return True
		            
		return False