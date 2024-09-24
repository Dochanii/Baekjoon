import sys
from collections import deque
input = sys.stdin.readline

def is_movable(dr,dc,n,m):
    if 0 <= dr and dr < n and 0 <= dc and dc < m:
        return 1
    return 0

def change_direction(d):
    if d == 0:
        return 3
    return d - 1

def move_front(direction,row,col):
   
    if direction == 0:
        dr = row-1
        if is_movable(dr,col,n,m) and area[dr][col] == 0:
            row = dr
    elif direction == 1:
        dc = col+1
        if is_movable(row,dc,n,m) and area[row][dc] == 0:
            col = dc
    elif direction == 2:
        dr = row + 1
        if is_movable(dr,col,n,m) and area[dr][col] == 0:
            row = dr
    elif direction == 3:
        dc = col-1
        if is_movable(row,dc,n,m) and area[row][dc] == 0:
            col = dc
    return row,col
        
def move_back(direction,row,col):
    is_possible = False
    if direction == 0:
        dr = row + 1
        if is_movable(dr,col,n,m) and area[dr][col] != 1:
            is_possible = True
            row = dr
    elif direction == 1:
        dc = col - 1
        if is_movable(row,dc,n,m) and area[row][dc]!=1:
            is_possible = True
            col = dc
    elif direction == 2:
        dr = row - 1
        if is_movable(dr,col,n,m) and area[dr][col]!=1:
            is_possible = True
            row = dr
    elif direction == 3:
        dc = col + 1
        if is_movable(row,dc,n,m) and area[row][dc]!=1:
            is_possible = True
            col = dc
    if is_possible:
        return row,col
    else:
        return False

n,m = map(int,input().split())
row, col, d = map(int,input().split())
 
area = []
for _ in range(n):
    area.append(list(map(int,input().split())))

direction_x = [1,0,-1,0]
direction_y = [0,1,0,-1]
direction = d

cnt = 0
# for _ in range(4):
while True:
    
    flag = 0
    if area[row][col] == 0:
        area[row][col] = 2
        cnt += 1
    # 현재 칸이 청소가 된 경우
    else:
        for i in range(4):
            dc = col + direction_x[i]
            dr = row + direction_y[i]
            
            #움직일 수 있는 경우
            if is_movable(dr, dc, n, m):  
                if area[dr][dc] == 0:
                    flag = 1
                    break
        if flag:
            direction = change_direction(direction)
            # print(direction)
            row,col = move_front(direction,row,col)
            # print(row,col)
            
        else:
            if move_back(direction,row,col)  == False:
                break
            else:
                row,col = move_back(direction,row,col)
print(cnt)