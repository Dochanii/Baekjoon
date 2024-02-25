import sys
n = int(sys.stdin.readline())
fac = 1
for i in range(1,n+1):
    fac *= i
cnt = 0
while fac>0:
    if fac%10 == 0:
        cnt+=1
    else:
        break
    fac//=10
print(cnt)
    