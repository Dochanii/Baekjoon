import sys
from collections import deque

input = sys.stdin.readline


T = int(input())


for _ in range(T):
    func = input().rstrip()  
    n = int(input())  
    arr = input().rstrip()[1:-1]

    
    if n == 0:
        queue = deque()
    else:
        queue = deque(arr.split(','))

    
    reverse_flag = False
    error_flag = False

    
    for command in func:
        if command == 'R':
            reverse_flag = not reverse_flag  
        elif command == 'D':
            if not queue:
                error_flag = True
                print("error")
                break
            if reverse_flag:
                queue.pop()  
            else:
                queue.popleft()


    if not error_flag:
        if reverse_flag:
            queue.reverse()
        print('[' + ','.join(queue) + ']')  
