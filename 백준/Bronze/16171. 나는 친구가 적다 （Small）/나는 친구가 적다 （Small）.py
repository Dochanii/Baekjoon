s = input()
k = input()

new_s = ''
for i in s:
    if'a'<=i and i<='z' or 'A'<=i and i<='Z':
        new_s+=i

if k in new_s:
    print(1)
else:
    print(0)