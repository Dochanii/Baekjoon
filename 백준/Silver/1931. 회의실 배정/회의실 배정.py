import sys
n = int(sys.stdin.readline())
coference_room = []
cnt = 0
for _ in range(n):
    input_data_1,input_data_2 = map(int, sys.stdin.readline().split())
    coference_room.append((input_data_1,input_data_2))
    
coference_room.sort(key=lambda x:(x[1],x[0]))

end = 0
for rooms in coference_room:
    if end<=rooms[0]:
        end = rooms[1]
        cnt+=1
print(cnt)

