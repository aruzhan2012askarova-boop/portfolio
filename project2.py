import re
import random
import time

# регистрация
user={}
cards={}
ochcki={}
current_user =None

class Program:
    def registration (self):
     global current_user,user,cards

     name_pattern = r'^[a-zA-Z0-9]+$'
     password_pattern = r'^[a-zA-Z0-9]+$'

     ima = input('Введите имя: ').lower()
     parol = input('Введите пароль: ')
    
     # Проверка имени
     if not re.fullmatch(name_pattern, ima):
      print('Имя должно содержать только латинские буквы, цифры и _.')
      return
     

     # Проверка пароля
     if len(parol) < 5 or not re.fullmatch(password_pattern, parol):
      print('Пароль должен быть минимум 5 символов и содержать только латинские буквы и цифры.')
      return
      
     current_user= ima
     #проверка в оперативной памяти
     if ima in user and user[ima]:
        print('такое уже есть!')
        return
     else:
        user[ima]= parol
        cards[ima]=[]
        ochcki[ima]=0
        print('ваш аккаунт успешно создан!')

    def vhod (self):
     global current_user
     #проверка и ввод
     name_pattern = r'^[a-zA-Z0-9_]+$'
     password_pattern = r'^[a-zA-Z0-9]+$'

     ima = input('Введите имя: ').lower()
     parol = input('Введите пароль: ')

     # Проверка имени
     if not re.fullmatch(name_pattern, ima):
      print('Имя должно содержать только латинские буквы, цифры и _.')
      exit()

     # Проверка пароля
     if len(parol) < 5 or not re.fullmatch(password_pattern, parol):
      print('Пароль должен быть минимум 5 символов и содержать только латинские буквы и цифры.')
      exit()
     
     if ima in user and user[ima]== parol:
        current_user=ima
        print('с возращением!')
     else:
        print('такого нету!зарегистрируйся!')
     

rabota_s_proectom=Program()
print('\n1-регистрация')
print('2-вход')
vibr=input('выберите:')
if vibr=='1':
    rabota_s_proectom.registration()
elif vibr =='2':
    rabota_s_proectom.vhod()
else:
    print('такое нельзя выбрать!')


# карточки

class Kartochka:

    def __init__(self):
        self.cards = []

    # добавить карточку
    def dobavit(self):
        global current_user
        
        if current_user is None:
           print('войди в аккаунт!')
           return
        vopros = input('Введите вопрос: ')
        otvet = input('Введите ответ: ')

        cards[current_user].append([vopros, otvet])

        print('Карточка добавлена!')


    # случайный вопрос
    def ran(self):
        global current_user
        if current_user is None:
           print('войди в аккаунт!')
           return
        
        if len(cards[current_user]) == 0:
            print('Карточек пока нет!')
            return

        card = random.choice(cards[current_user])

        print('\nВопрос:')
        print(card[0])

        otvet = input('Ваш ответ: ')

        if otvet.lower() == card[1].lower():
            print('Правильно!')
        else:
            print('Неправильно!')
            print('Правильный ответ:', card[1])

    # викторина с таймером
    def victorina(self):

        global current_user

        if len(cards[current_user]) < 3:
            print('Карточек недостаточнобнужно минимум 3!')
            return
        
        quiz = random.sample(cards[current_user],3)
        print('\nУ вас 30 секунд!')
        start = time.time()
        for card in quiz:
         
         if time.time() - start>30:
           print('вермя вышло!')
           break
         print('Вопрос:', card[0])
         otvet = input('Ответ: ')


         if otvet.lower() == card[1].lower():
            print('Верно!')
            ochcki[current_user] += 3
         else:
            print('Неверно!')
            print('Правильный ответ:', card[1])
        
        print('Очки:', ochcki[current_user])

    def vhod (self):
     global current_user
     #проверка и ввод
     name_pattern = r'^[a-zA-Z0-9_]+$'
     password_pattern = r'^[a-zA-Z0-9]+$'

     ima = input('Введите имя: ').lower()
     parol = input('Введите пароль: ')

     # Проверка имени
     if not re.fullmatch(name_pattern, ima):
      print('Имя должно содержать только латинские буквы, цифры и _.')
      exit()

     # Проверка пароля
     if len(parol) < 5 or not re.fullmatch(password_pattern, parol):
      print('Пароль должен быть минимум 5 символов и содержать только латинские буквы и цифры.')
      exit()
     
     if ima in user and user[ima]== parol:
        current_user=ima
        print('с возращением!')
     else:
        print('такого нету!зарегистрируйся!')
     
    def registration (self):
     global current_user,user,cards

     name_pattern = r'^[a-zA-Z0-9]+$'
     password_pattern = r'^[a-zA-Z0-9]+$'

     ima = input('Введите имя: ').lower()
     parol = input('Введите пароль: ')
    
     # Проверка имени
     if not re.fullmatch(name_pattern, ima):
      print('Имя должно содержать только латинские буквы, цифры и _.')
      return
     

     # Проверка пароля
     if len(parol) < 5 or not re.fullmatch(password_pattern, parol):
      print('Пароль должен быть минимум 5 символов и содержать только латинские буквы и цифры.')
      return

     current_user= ima
     #проверка в оперативной памяти
     if ima in user and user[ima]:
        print('такое уже есть!')
        return
     else:
        user[ima]= parol
        cards[ima]=[]
        ochcki[ima]=0
        print('ваш аккаунт успешно создан!')


# Выбирание игр,счет очков

game = Kartochka()

while True:

    print('\n1 - Добавить карточку')
    print('2 - Случайный вопрос')
    print('3 - Викторина')
    print('4 - создание другого аккаунта')
    print('5 - смена аккаунта')
    print('6 - Выход')
    vibor = input('Что выбрать?: ')

    if vibor == '1':
        game.dobavit()

    elif vibor == '2':
        game.ran()

    elif vibor == '3':
        game.victorina()

    elif vibor =='4':
       game.registration()

    elif vibor == '5':
        game.vhod()

    elif vibor == '6':
        print('Пока!')
        break
        
    else:
        print('Неверный выбор!')