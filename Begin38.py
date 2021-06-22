#Begin38. A va B koeffisentlari berilgan, Ax+B=0 chiziqli tenglamaning yechimini (x ni)
#aniqlaydigan programma tuzilsin.(A!=0)

A=float(input('A='))
B=float(input('B='))

if A==0 and B==0:
    print('Tenglama cheksiz ko\'p yechimga ega')
elif A==0:
    print('Tenglama yechimga ega emas')
else:
    x=-B/A
    print('X=',x)
