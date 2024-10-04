import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

queue = deque()
visited = [0] * 100001
# 곱하기 2, +1 ,-1 순서
queue.append([0,n])

res = 0

while queue:
    current_info = queue.popleft()
    
    time, current_pos = current_info

    if current_pos == k:
        res = current_pos
        break
    # 곱하기 2
    changed_pos = current_pos * 2
    if 0<= changed_pos <= 100000 and visited[changed_pos] == 0:
        queue.append([0,changed_pos])
        visited[changed_pos] = visited[current_pos]
        if changed_pos == k:
            res = changed_pos
            break
    # -1
    changed_pos = current_pos - 1
    if 0<= changed_pos <= 100000 and visited[changed_pos] == 0:
        queue.append([1,changed_pos])
        visited[changed_pos] = visited[current_pos] + 1
        if changed_pos == k:
            res = changed_pos
            break
    
    # +1
    changed_pos = current_pos + 1
    if 0<= changed_pos <= 100000 and visited[changed_pos] == 0:
        queue.append([1,changed_pos])
        visited[changed_pos] = visited[current_pos] + 1
        if changed_pos == k:
            res = changed_pos
            break
    
    
    
print(visited[res])