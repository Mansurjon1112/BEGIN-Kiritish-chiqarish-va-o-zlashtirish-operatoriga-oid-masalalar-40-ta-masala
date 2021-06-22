#Begin35. Qayiqning tezligi V, daryo oqimining tezligi U, (V>U). Qayiqning daryo
#oqimi bo`yicha harakatlanish vaqti T1, oqimga qarshi T2 . Qayiqni yurgan S yo`lini aniqlovchi
#programma tuzilsin.

v=int(input('Qayiqning tezligi ='))
u=int(input('Daryo oqimining tezligi ='))
t1=int(input('Oqim bo\'yicha harakatlanish vaqti ='))
t2=int(input('Oqimga qarshi harakatlanish vaqti ='))
if v>u:
    s=(v+u)*t1+(v-u)*t2
    print('Qayiqning yurgan yo\'li ',s)
else:
    print('Oqim tezligi qayiq tezligidan katta bo\'lmasligi kerak!')
    
