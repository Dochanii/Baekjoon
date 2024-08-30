import sys
input = sys.stdin.readline

S = set([])

M = int(input())
all_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for _ in range(M):
    input_order = input().split()
    
    if input_order[0] == 'all':
        S.clear()
        S.update(set(all_list))
    elif input_order[0] == 'empty':
        S.clear()
    else:
        x = int(input_order[1])
        
        if input_order[0] == 'add':
            if x in S:
                pass
            else:
                S.add(x)
        elif input_order[0] == 'check':
            
            if x in S:
                print(1)
            else:
                print(0)
        elif input_order[0] == 'remove':
            if x in S:
                S.remove(x)
            else:
                pass
        elif input_order[0] == 'toggle':
            if x in S:
                S.remove(x)
            else:
                S.add(x)
       
    
