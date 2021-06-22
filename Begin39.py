#Begin39. A, B, C koeffisentlari berilgan,Ax^2+Bx+C=0 kvadrat tenglamaning diskriminanti noldan
#katta bo`lsa uning yechimlarini aniqlaydigan programma tuzilsin.

A=float(input('A='))
B=float(input('B='))
C=float(input('C='))
D=B*B-4*A*C
if D>=0:
    print('Tenglama yechimga ega')
    x1=(-B+D**0.5)/2
    x2=(-B-D**0.5)/2
    if D==0:
        print('x1 =',x1)
    else:
        print('x1 =',x1,'x2 =',x2)
else:
    print('Tenglama yechimga ega emas')

    
