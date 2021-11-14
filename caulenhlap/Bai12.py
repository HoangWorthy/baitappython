import math as m
n = int(input('Nhap so nguyen duong n: '))
if n < 0 : exit
c = True
for i in range(2,int(m.sqrt(n))+1):
    if n % i == 0: c = False
if c :print(n,'la so nguyen to')
else :print(n,'khong phai la so nguyen to')