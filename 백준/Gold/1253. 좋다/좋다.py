import sys
input = sys.stdin.readline

n  = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0
for idx, target in enumerate (arr):
    temp_list = arr[:idx] + arr[idx+1:]
    first , end = 0, len(temp_list)-1
    while first < end:
        temp = temp_list[first] + temp_list[end]
        if temp == target:
            cnt +=1
            break
        elif temp < target:
            first +=1
        else:
            end -=1


    
print(cnt)