#Begin21. Uchburchakning uchta tomoni uchlari koordinatlari berilgan . Ikki
#nuqta orasidagi masofani topish Begin20 da berilgan. Uchburchakning yuzasini va perimatrini
#toping.

x1=int(input('x1='))
y1=int(input('y1='))
x2=int(input('x2='))
y2=int(input('y2='))
x3=int(input('x3='))
y3=int(input('y3='))
a = ((x1-x2)**2 +(y1-y2)**2)**(0.5)
b = ((x1-x3)**2 +(y1-y3)**2)**(0.5)
c = ((x3-x2)**2 +(y3-y2)**2)**(0.5)
if (a+b>c) and (a+c>b) and (b+c>a):
    p=a+b+c
    yp=p/2
    s=(yp*(yp-a)*(yp-b)*(yp-c))**0.5
    print('Uchburchak yuzi',s,'Perimetri',p)
else:
    print('Uchburchak hosil qilib bo\'lmaydi')

