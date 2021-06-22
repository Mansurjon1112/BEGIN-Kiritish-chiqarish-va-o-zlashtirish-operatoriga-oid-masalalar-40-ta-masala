#Begin40. A1, B1,C1, A2, B2, C2 koeffisentlari berilgan, chiziqli tenglamalar sistemasi yechimlarini
#aniqlaydigan programma tuzilsin

A1=float(input('A1='))
B1=float(input('B1='))
C1=float(input('C1='))
A2=float(input('A2='))
B2=float(input('B2='))
C2=float(input('C2='))

if (A1/A2)!=(B1/B2):
    D=A1*B2-A2*B1
    X=(C1*B2-C2*B1)/D
    Y=(C2*A1-A2*C1)/D
    print('x =',x,'y =',y)
elif  (A1/A2)==(B1/B2)!=(C1/C2):
    print('Yechimga ega emas')
else:
    print('Cheksiz ko\'p yechimga ega')


