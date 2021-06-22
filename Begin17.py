#Sonlar o`qida A, B, C nuqtalar berilgan. AC va BC kesmalarning uzunligini va kesmalar
#uzunligining yig`indisini topuvchi programma tuzilsin.

a=int(input('A = '))
b=int(input('B = '))
c=int(input('C = '))
ab=abs(a-b)
bc=abs(b-c)
yig = ab+bc
print('AB =',ab,'BC =',bc,"Yig'indisi",yig)
