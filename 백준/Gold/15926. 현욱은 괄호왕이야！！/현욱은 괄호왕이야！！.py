import sys
from collections import deque

n = int(sys.stdin.readline())
stack = []
parenthisis = sys.stdin.readline().rstrip()
temp_lst = []

for i in range(0,len(parenthisis)):
    if parenthisis[i] == '(':
        stack.append((i,parenthisis[i]))
        temp_lst.append(0)
        
    elif parenthisis[i] == ')':
        if stack:
            temp_lst[stack[-1][0]] = 1
            stack.pop()
            temp_lst.append(1)
        else:
            temp_lst.append(0)
        
cnt = 0
max_cnt = 0

for i in temp_lst:
    if i == 1:
        cnt +=1
    else:
        if max_cnt<cnt:
            max_cnt = cnt
        cnt = 0
if max_cnt<cnt:
            max_cnt = cnt
print(max_cnt)
            
        

    
# 12
# (()(()()(()(
# 011011110110
# 
    