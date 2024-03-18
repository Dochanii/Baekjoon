import sys
from collections import deque


h,w = map(int, sys.stdin.readline().split())
blocks = list(map(int,sys.stdin.readline().split()))

 

res_lst = []

for i in range(1,len(blocks)-1):
    left_max = max(blocks[:i])
    right_max = max(blocks[i+1:])
    
    short_block = min(left_max,right_max)
    
    if blocks[i]< short_block:
        res_lst.append(short_block-blocks[i])

print(sum(res_lst))

