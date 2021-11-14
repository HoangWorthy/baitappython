n = int(input('Nhap so nguyen duong n: '))
if n < 0 : exit
c = 0
for i in range(2,n+1,2):
    c+=i
print(f'Tong cac so chan tu 1 den {n} la: {c}')