dots=int(input())
sp=[[int(i) for i in input().split()] for _ in range(dots)]
sp_res=[0,0,0,0]
for i in sp:
       if i[0]>0:
           if i[1]>0:
               sp_res[0] += 1
           else:
               sp_res[3] += 1
       else:
           if i[1]>0:
               sp_res[1] += 1
           else:
               sp_res[2] += 1
print(f'Первая четверть: {sp_res[0]}')
print(f'Вторая четверть: {sp_res[1]}')
print(f'Третья четверть: {sp_res[2]}')
print(f'Четвертая четверть: {sp_res[3]}')