import sys
from collections import deque
input = sys.stdin.readline

n,w,l = map(int,input().split())
trucks = deque(map(int,input().split()))
bridge = [0]*w

cnt = 0

while bridge:
    cnt += 1
    bridge.pop(0)
    if trucks:
        if sum(bridge) + trucks[0] <= l:
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)
            
print(cnt)

        
        
    
        
        