import sys
import heapq

input = sys.stdin.readline

n = int(input())

lecture_time = []
for _ in range(n):
    s,t = map(int,input().split())
    lecture_time.append((s,t))

lecture_time.sort(key=lambda x : (x[0],x[1]))

heap = [lecture_time[0][1]]

for i in range(1,n):
    if lecture_time[i][0] >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, lecture_time[i][1])

print(len(heap))