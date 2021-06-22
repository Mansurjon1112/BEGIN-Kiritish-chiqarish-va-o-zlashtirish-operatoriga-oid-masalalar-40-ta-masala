#Begin28. A soni berilgan. A ning A^2, A^3, A^5,A^10,A^15 darajalarini aniqlovchi programma tuzilsin.

a=float (input('A='))

a2=a*a      #a2=a**2
a3=a2*a     #a3=a**3
a5=a2*a3    #a5=a**5
a10=a5*a5   #a10=a**10
a15=a10*a5  #a15=a**15

print('Kvadrati',a2,'\nUchinchi darajasi',a3,'\nBeshinchi darajasi',a5)
print('O\'ninchi darajasi',a10,'\nO\'nbeshinchi darajasi',a15)
