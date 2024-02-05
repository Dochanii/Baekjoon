import sys
n = int(sys.stdin.readline())
res_lst = []
lst = {}
for _ in range(n):
    files = input().split('.')
    temp = (files[1])
    if temp in lst:
        lst[temp] +=1
    else:
        lst.setdefault(temp,1)
res_lst = sorted(lst.items())
for i in res_lst:
    print(i[0], i[1])
