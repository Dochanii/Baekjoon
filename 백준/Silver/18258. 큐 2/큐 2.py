import sys
from collections import deque
n = int(sys.stdin.readline())
que = deque()
for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        que.append(int(order[1]))
    elif order[0] == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(que))
    elif order[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    else:
        if que:
            print(que[-1])
        else:
            print(-1)
