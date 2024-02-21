import sys
parenthesis = sys.stdin.readline().rstrip()
stack = []
is_close = False
res = 0

for i in parenthesis:        
    if i=='(':
        stack.append(i)
        is_close=False

    else:
        stack.pop()
        if is_close:
            res+=1
        else:
            res+=len(stack)
        is_close = True
        
print(res)
        
    
    
    
