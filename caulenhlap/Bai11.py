n = int(input('Nhap so nguyen duong n: '))
if n < 0 : exit
c = 0
print(f'Cac uoc that su cua {n} la: ',end=' ')
for i in range(1,n):
    if n % i == 0:
        c+=i
        print(i,end=' ')
if c == n : print(f'\n{n} la so hoan hao')
else : print(f'\n{n} khong phai la so hoan hao')