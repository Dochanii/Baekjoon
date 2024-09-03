import sys
from collections import deque
input = sys.stdin.readline

Queue = deque()

def bfs():
    cnt = 0
    while(Queue):
        cur_r,cur_c = Queue.popleft()
        for i in enumerate(virus[cur_c]):
            if i[1] == 1 and visited[i[0]] == False:
                Queue.append((cur_r,i[0]))
                visited[i[0]] = True
                cnt += 1
    print(cnt)
    

computers = int(input())
v = int(input())


virus = [[0]*(computers+1)  for _ in range(computers+1)]
visited = [False]*(computers+1)



for i in range(v):
    r,c = map(int,input().split())
    if r>0 and r<=computers and c>0 and c<=computers:
        virus[r][c] = 1
        virus[c][r] = 1

Queue.append((1,1))
visited[1] = True

bfs()

