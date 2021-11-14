n = int(input('Nhap so nguyen duong n: '))
if n < 0 : exit
c = 0
print('S =',end=' ')
for i in range(1,n+1):
    c+=i
    if i == n: 
        print(i,end=' ')
        break
    print(f'{i} +',end=' ')
print(f'= {c}')