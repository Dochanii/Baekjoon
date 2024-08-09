import sys
input = sys.stdin.readline
import heapq

n = int(input())
max_heap = []

for _ in range(n):
    order = int(input())
    
    if order == 0:
        if max_heap:
            print(-heapq.heappop(max_heap))  
        else:
            print(0)
    elif order > 0:
        heapq.heappush(max_heap, -order)  
