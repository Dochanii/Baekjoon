import sys
from collections import deque

input = sys.stdin.readline

def is_movable(dr,dc,n,m):
    if (dr>=0 and dr<m) and (dc>=0 and dc<n):
        return True
    return False
def change_direction(direction):
    return (direction + 1) % 4
    
    


n, m = map(int, input().split())

tomato_box = []

for _ in range(m):
    tomato_box.append(list(map(int, input().rstrip().split())))
    
direction_x = [1,0,-1,0]
direction_y = [0,1,0,-1]

direction = 0

queue = deque()

for i in range(m):
    for j in range(n):
        if tomato_box[i][j] == 1:
            queue.append((i,j))

# 현재 좌표에서 움직일 수 있는 좌표를 큐에 다 담아야되는 로직 필요
# 현재 좌표에서 움직일 수 없으면 큐에서 꺼내야됨(bfs)


while queue:
    
    cur = queue.popleft()
    
    
    # dc = col + direction_x[direction]
    # dr = row + direction_y[direction]
    
    for i in range(4):
        row = cur[0]
        col = cur[1]
    
        dc = col + direction_x[i]
        dr = row + direction_y[i]
    
        if(is_movable(dr,dc,n,m) and tomato_box[dr][dc]==0):
            tomato_box[dr][dc] += tomato_box[row][col] + 1
        
            queue.append((dr,dc))
        
is_mature = True

day = 0



for tomato_x in tomato_box:
    for tomato in tomato_x:
        if tomato == 0:
                 is_mature = False
                 break
    day = max(day,max(tomato_x))


if not is_mature:
    print(-1)
else:
    print(day-1)
