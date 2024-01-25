strings = [input() for _ in range(5)]

len_lst = []
res = ''
for row in range(len(strings)):
    len_lst.append(len(strings[row]))

for row in range (max(len_lst)):
    for col in range (5):
        if row < len_lst[col]:
            res += strings[col][row]
print(res)