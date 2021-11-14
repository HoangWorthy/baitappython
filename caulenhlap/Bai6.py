n = int(input('Nhap so nguyen duong n: '))
if n < 0 : exit
c = 0
for i in range(1,n+1):
    c+=i
print(f'Tong cac so tu 1 den {n} la',c)