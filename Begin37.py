#Begin37. Birinchi avtomabilning tezligi V1, ikkinchisiniki V2, ular orasidagi masofa
#S. Ular biri–biri tomonga harakatlana boshlasa T vaqtdan keyin ular orasidagi masofani aniqlaydigan
#programma tuzilsin.

v1=int(input('Birinchi avtomobilning tezligi ='))
v2=int(input('Ikkinchi avtomobilning tezligi ='))
s=int(input('Ular orasidagi masofa ='))
t=int(input('Vaqt ='))

v=v1+v2 #umumiy tezlikni topish
masofa=s-v*t #orasidagi masofa

if masofa>0:
    print('ular orasidagi masofa',masofa)
else:
    t=s/(v1+v2) #uchrashish vaqtini aniqlash
    print('Ular ',t,' soatdan keyin uchrashishgan')
