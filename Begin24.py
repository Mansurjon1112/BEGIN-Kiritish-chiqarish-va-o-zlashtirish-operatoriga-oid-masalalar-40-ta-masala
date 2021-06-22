#Begin24. A, B va C sonlari berilgan. A ni qiymati C ga, C ni qiymati B ga va B ni qiymati A ga
#almashtirilsin. A, B va C ning yangi qiymatilari ekranga chiqarilsin.

a=int(input('A='))
b=int(input('B='))
c=int(input('C='))
#1-usul
a,b,c=c,a,b

#2-usul
'''m=a
a=c
c=b
b=m'''

print('A =',a,'B =',b,'C =',c)
