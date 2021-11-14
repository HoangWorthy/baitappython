n = str(input('Nhap so nguyen duong n: '))
if int(n) < 0 : exit
c = 0
for i in n:
    c+=int(i)
print('S =',c)