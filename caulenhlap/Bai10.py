n = int(input('Nhap so nguyen duong n: '))
if n < 0 : exit
print(f'Cac uoc that su cua {n} la: ',end=' ')
for i in range(1,n):
    if n % i == 0: print(i,end=' ')