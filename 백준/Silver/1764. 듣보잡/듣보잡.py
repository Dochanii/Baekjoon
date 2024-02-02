import sys
n,m = map(int ,sys.stdin.readline().split())
d = [input() for _ in range(n)]
b = [input() for _ in range(m)]
res_lst = list(set(d) & set(b))
res_lst.sort()
print(len(res_lst))
for i in res_lst:
    print(i)