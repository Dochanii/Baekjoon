n = int (input())
list1 = []
list2 = []
for i in range(n):
    list1.append(int(input()))
list1.sort()

for i in range(0,n,1):
    list2.append(int(list1[i])*(n-i))

print(max(list2))

   
