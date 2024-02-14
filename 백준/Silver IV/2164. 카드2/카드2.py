import sys
from collections import deque

n = int(sys.stdin.readline())
deq = deque(range(1,n+1))
for _ in range(n):
    if(len(deq)==1):
        break
    deq.popleft()
    deq.rotate(-1)
res = deq[0]
print(res)
    