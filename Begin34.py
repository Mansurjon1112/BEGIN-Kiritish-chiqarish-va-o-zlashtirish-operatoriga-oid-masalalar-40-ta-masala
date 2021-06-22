#Begin34. X kg shokolad A so`m turadi va Y kg konfet B so`m turadi. 1 kg shokolad 1 kg konfetdan
#qancha qimmat turishini aniqlovchi programma tuzilsin.

x = int(input('x='))
A = int(input('A='))
y = int(input('y='))
B = int(input('B='))

sh = A/x
k = B/y

if sh==k:
    print('Shokolad va konfet narxlari teng')
elif sh>k: 
    print('Shokolad konfetdan  ',sh-k,' qimmat')
else:
    print('Shokolad konfetdan  ',k-sh,' arzon')

