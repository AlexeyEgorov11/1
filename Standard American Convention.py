r = list(input())[::-1]
new = []
c = 0
for i in range(len(r)-1):
    new.append(r[i])
    c += 1
    if c == 3:
        new.append(',')
        c = 0
new.append(r[-1])
print(''.join(new[::-1]))
