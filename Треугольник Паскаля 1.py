n = int(input())
f_s = [0, 1, 0]
print(1)
for k in range(n-1):
    next_s = []
    for i in range(len(f_s)-1):
        next_s.append(f_s[i]+f_s[i+1])
    next_s.append(0)
    next_s = [0] + next_s
    f_s = next_s
    print(*f_s[1:-1])
