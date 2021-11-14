m = int(input())
n = int(input())
if m >= n: exit
c = 0
for i in range(m,n+1):
    if i % 2 != 0: c+=i
print(f'Tong cac so le tu {m} den {n} la: {c}')