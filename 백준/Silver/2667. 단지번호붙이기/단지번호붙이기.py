import sys
from collections import deque

def is_movable(n,dr,dc):
    if 0<= dr and dr< n and 0<= dc and dc<n:
        return 1
    return 0

def bfs(row,col):
    home_cnt = 0
    
    while Queue:
        row,col = Queue.popleft()
        
        
        direction_x = [1,0,-1,0]
        direction_y = [0,1,0,-1]
        
        for i in range(4):
            dr = row + direction_y[i]
            dc = col + direction_x[i]
            
            if is_movable(n,dr,dc) and graph[dr][dc] == 1 and visited[dr][dc] == False:
                Queue.append((dr,dc))
                visited[dr][dc] = True
                home_cnt += 1
    return home_cnt
        
        
input = sys.stdin.readline

n = int(input())
Queue = deque()

graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

row = 0
col = 0
cnt = 0

home_arr = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            row = i
            col = j
            Queue.append((row,col))
            visited[row][col] = True
            home_arr.append(bfs(row,col) + 1)
            cnt += 1
    
print(cnt)
home_arr.sort()
for hc in home_arr:
    print(hc)
 