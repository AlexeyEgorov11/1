sp=[int(i) for i in input().split()]
c=0
for i in range(len(sp)-1):
    if sp[i]<sp[i+1]:
        c+=1
print(c)