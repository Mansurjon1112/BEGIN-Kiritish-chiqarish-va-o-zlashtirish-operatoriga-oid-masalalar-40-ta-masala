#Sonlar o`qida A, B, C nuqtalar berilgan. C nuqta A va B nuqtalar orasida joylashgan. AC
#va BC kesmalar uzunligining ko`paytmasini toping.

a=int(input('A = '))
b=int(input('B = '))
c=int(input('C = '))
if a<c and b>c:
    ac=abs(a-c)
    bc=abs(b-c)
    kup = ac*bc
    print('AC =',ac,'BC =',bc,"Ko'paytmasi",kup)
else:
    print('C nuqta A va B nuqtalar orasida joylashmagan')
