import sys
from collections import deque

input = sys.stdin.readline

def bfs(index):
    Queue = deque([index])  
    visited[index] = True   
    while Queue:
        cur = Queue.popleft()  
        for i in range(1, n + 1):
            if graph[cur][i] == 1 and not visited[i]:
                Queue.append(i)  
                visited[i] = True 

Queue = deque()

n,m = map(int,input().split())


graph = [[0]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    u,v = map(int,input().split())
    graph[u][v] = 1
    graph[v][u] = 1
    
cnt=  0
for i in range(1,n+1):
    if visited[i] == False:
        bfs(i)
        cnt += 1
print(cnt)
