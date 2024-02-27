import sys

n = int(sys.stdin.readline())
arr = []
freq_lst = []
for i in range(n):
    num = int(sys.stdin.readline())
    arr.append(num)
print(round(sum(arr)/n))
arr.sort()
print(arr[n//2])
dic = dict()
for i in arr:
    if i in dic:
        dic[i] +=1
    else:
        dic[i]=1
max = max(dic.values())
for i in dic:
    if max == dic[i]:
        freq_lst.append(i)
if len(freq_lst)>1:
    print(freq_lst[1])
else:
    print(freq_lst[0])

print(arr[n-1]-arr[0])
        