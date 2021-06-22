#Begin23. A, B va C sonlari berilgan. A ni qiymati B ga, B ni qiymati C ga va C ni qiymati A ga
#almashtirilsin. A, B va C ning yangi qiymatilari ekranga chiqarilsin.

a=int(input('A='))
b=int(input('B='))
c=int(input('C='))
#1-usul
# a,b,c=b,c,a

#2-usul
m=a
a=b
b=c
c=m

print('A =',a,'B =',b,'C =',c)
