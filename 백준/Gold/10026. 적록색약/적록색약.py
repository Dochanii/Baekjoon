import sys
from collections import deque

input = sys.stdin.readline

def is_movable(dr,dc,N):
    if(0<=dr and dr < N )and (0<=dc and dc<N):
        return True
    return False


        


N = int(input())

rgb_list = [list(input()) for _ in range(N)]
visited_list = [[False]*N for _ in range(N)]


Q = deque()

direction_x=[1,0,-1,0]
direction_y=[0,1,0,-1]

person = 0
disabled_person = 0

for i in range(N):
    for j in range(N):
        if not visited_list[i][j]:
            Q.append((i,j))
            visited_list[i][j] = True
            while Q:
                cur = Q.popleft()
                row = cur[0]
                col = cur[1]
                
                for direction in range(4):
                    dr = row + direction_y[direction]
                    dc = col + direction_x[direction]
                    
                    if(is_movable(dr,dc,N) and (rgb_list[dr][dc] == rgb_list[row][col]) and visited_list[dr][dc] == False):
                        visited_list[dr][dc] = True
                        Q.append((dr,dc))
            person +=1

# print(person)

for i in range(N):
    for j in range(N):
        if rgb_list[i][j] == 'G':
            rgb_list[i][j] = 'R'
            
visited_list = [[False]*N for _ in range(N)]
Q.clear()


for i in range(N):
    for j in range(N):
        if not visited_list[i][j]:
            Q.append((i,j))
            visited_list[i][j] = True
            while Q:
                cur = Q.popleft()
                row = cur[0]
                col = cur[1]
                
                for direction in range(4):
                    dr = row + direction_y[direction]
                    dc = col + direction_x[direction]
                    
                    if(is_movable(dr,dc,N) and (rgb_list[dr][dc] == rgb_list[row][col]) and visited_list[dr][dc] == False):
                        visited_list[dr][dc] = True
                        Q.append((dr,dc))
            disabled_person += 1

print(person, disabled_person)

            
                



