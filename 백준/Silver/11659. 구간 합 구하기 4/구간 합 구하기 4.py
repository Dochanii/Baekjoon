import sys
input = sys.stdin.readline

n,m = map(int,input().split())

datas = list(map(int,input().split()))

sum = [0]
temp = 0

for i in datas:
    temp += i
    sum.append(temp)
    

for _ in range(m):
    i,j = map(int,input().split())
    print(sum[j]-sum[i-1])
    