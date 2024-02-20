import sys
n = int(sys.stdin.readline())
sequence = [x for x in range(n,0,-1)]

stack = []
res=[]
prev_num = 0
max = 0
res_tag = False
for _ in range(n):
    num = int(sys.stdin.readline())
   
    if prev_num>num:
        if stack[-1]!=num:
            res_tag = True
        stack.pop()
        res.append('-')
    else:
        for i in range(max,num):
            stack.append(sequence.pop())
            res.append('+')
        stack.pop()
        res.append('-')
        
    if max<num:
        max = num
    prev_num = num
if not res_tag:
    for i in res:
        print(i)
else:
    print("NO")
    
    
                
                
        