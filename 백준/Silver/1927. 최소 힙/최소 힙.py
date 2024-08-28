import sys
import heapq

input = sys.stdin.readline
heap =[]

N = int(input())

for _ in range(N):
    num = int(input())
    if num == 0:
        if heap:
            print_num = heapq.heappop(heap)
            print(print_num)
        else:
            print(0)
    else:
        heapq.heappush(heap, num)