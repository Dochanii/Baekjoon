import sys
from collections import deque
T = int(sys.stdin.readline())
idx =0 
for _ in range(T):
    n,m = map(int, sys.stdin.readline().split())
    cnt = 0
    queue = deque()
    queue.extend(map(int, sys.stdin.readline().split()))
    while queue:
        max_q = max(queue)
        front = queue.popleft()
        m-=1
        
        if max_q == front:
            cnt+=1
            if m<0:
                print(cnt)
                break
        else:
            queue.append(front)
            if m<0:
                m = len(queue) - 1