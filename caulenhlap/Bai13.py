n = int(input('Nhap so nguyen duong n: '))
if n < 0 or n > 100 : exit
c = 1
for i in range(1,n+1):
    c*=i
print(f'{n}! = {c}')
#def giaithua(n):
#    if n == 0:
#        return 1
#    return n * giaithua(n-1)
#print(f'{n}! =',giaithua(n))