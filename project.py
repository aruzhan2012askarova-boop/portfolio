import random

hod_komputera=['камень','ножницы','бумага']

ochki_igroka=0
ochki_komputera=0

while ochki_komputera !=3 and ochki_igroka != 3:
    hod=random.choice(hod_komputera)
    print(hod)
    hod_igroka=input('Готов сыграть? тогда ходи!').strip().lower()
    if hod == 'камень' and hod_igroka=='ножницы':
     ochki_komputera +=1
     print(ochki_komputera,ochki_igroka)
    
    elif hod_igroka=='камень'and hod=='ножницы':
     ochki_igroka +=1
     print(ochki_komputera,ochki_igroka)
    
    elif hod=='бумага' and hod_igroka=='камень':
     ochki_komputera +=1
     print(ochki_komputera,ochki_igroka)

    elif hod_igroka=='бумага' and hod=='камень':
     ochki_igroka +=1
     print(ochki_komputera,ochki_igroka)
    
    elif hod=='ножницы' and hod_igroka=='бумага':
     ochki_komputera +=1
     print(ochki_komputera,ochki_igroka)

    elif hod_igroka=='ножницы' and hod=='бумага':
     ochki_igroka +=1
     print(ochki_komputera,ochki_igroka)
    else:
      print('ничья!')

print('И так, счет:',ochki_igroka,'-',ochki_komputera)
 
if ochki_komputera>ochki_igroka:
      print('Я победил! не хочешь сыграть еще раз?')
else:
      print('Ты победил! Поздравляю!')

