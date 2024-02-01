import sys
from collections import deque
n = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))
stack = []
res_lst = []
res_lst.append(0)
stack.append((0,top[0]))

for i in range(1,len(top)):
    while stack:
        if stack[-1][1]<top[i]:
            stack.pop()
        else:
            res_lst.append(stack[-1][0]+1)
            break
    if not stack:
        res_lst.append(0)
    stack.append((i,top[i]))
print(' '. join(map(str,res_lst)))