import sys
n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    temp = sys.stdin.readline().split()
    lst.append((int(temp[0]),temp[1]))
lst.sort(key=lambda x:x[0])
for i in lst:
    print(*i)