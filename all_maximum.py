# films = ['Матрица', 'Терминатор', 'Человек паук']
import math


# cords = [[2, 4], [2, 2], [1, 5]]
#
# print(films[])

# -----ДОБАВИТЬ-----

# films = []
# film_1 = input('введите фильм ')
# film_2 = input('введите фильм ')
# film_3 = input('введите фильм ')
#
# films.append(film_1)
# films.append(film_2)
# films.append(film_3)
#
# print(films)

# -----ФАКТЫ-----

# chislo = int(input('введите номер факта '))
# fact1 = ['хамелеоны могу двигать глазами в разных направлениях одновременно']
# fact2 = ['змеи видят через веки']
# fact3 = ['у коал отпечатки пальцев похожи на человеческие']
# fact4 = ['белые меведи - левши']
# fact5 = ['меня зовут Стас']
# facts = [fact1, fact2, fact3, fact4, fact5]
# print(facts[chislo-1])

# -----УБРАТЬ-----

# score = [5, 5, 5, 3, 4, 1, 4]
# print(score)
# score.remove(1)
# print(score)

# -----СОРТИРОВКА-----

# score = [5, 5, 5, 3, 4, 1, 4]
# print(score)
# score.sort()
# print(score)
# score.sort(reverse=1)
# print(score)

# -----ВОЗВРАТ ИНДЕКСА-----

# score = [5, 5, 5, 3, 4, 1, 4]
# i = score.index(4)
# print(i)

# -----ОЧИСТКА-----

# score = [5, 5, 5, 3, 4, 1, 4]
# print(score)
# score.clear()
# print(score)

# -----СТАТИСТИКА-----

# stat = [5, 4, 4, 2, 3, 4, 5, 2, 3, 3, 5]
# sr = sum(stat)/len(stat)
# maxi = max(stat)
# mini = min(stat)
# five = stat.count(5)
# print('средняя ', sr)
# print('максимальная ', maxi)
# print('минимальная ', mini)
# print('кол-во 5 = ', five)

# -----СРЕЗ-----

# # list[start:stop:step]
# score = [5, 5, 5, 3, 4, 1, 4]
# print(score)
# # score = [5, 5, 5, -- 3, 4, 1, --- 4]
# # последний элемент не включается
# print(score[3:6])

# -----ДОМАШКА НОМЕР 3-----

# score = ['яблоко', 'морковка', 'огурец', 'помидор', 'капуста']
# score.append('груша')
# score.remove(score[1]), score.insert(1, 'лук')
# print(len(score))
# score.sort()
# score.remove(score[-1])

# -------------------------------------------------------------------------

# ----------БИБЛИОТЕКИ----------

# -----RANDOM-----

# import random
# a=[1,2,3,4,5,6]
# r=random.choice(a)
# r=random.randint(1,100)
# print(r)

# import random
#
# fact1 = ['хамелеоны могу двигать глазами в разных направлениях одновременно']
# fact2 = ['змеи видят через веки']
# fact3 = ['у коал отпечатки пальцев похожи на человеческие']
# fact4 = ['белые меведи - левши']
# fact5 = ['меня зовут Стас']
# facts = [fact1, fact2, fact3, fact4, fact5]
# print(random.choice(facts))

# -----MATH-----

# import math
# m=math.isqrt(36)
# print(m)

# -----OS-----

# import os
# os.mkdir('new')

# -----FOR-----

# films = []
# for i in range(9):
#     film_1 = input('введите фильм ')
#     films.append(film_1)
# print(films)

# summa=0
# for i in range(6):
#     a=int(input('введите сумму '))
#     summa+=a
# print(summa*0.3)
#
# summa= []
# for i in range(6):
#     a=int(input('введите сумму '))
#     summa.append(a)
# print(sum(summa)*0.3)

# print('введите температуру за неделю')
# b=0
# for i in range(7):
#     a = int(input('ввод '))
#     b += a
# print('средняя температура равна ',b//7 )


# -----IF ELSE ELIF-----

# favorite_actor = 'Райан Гослинг'
# actor = input('введите главного актёра из фильма ')
# if actor == favorite_actor:
#     print('этот фильм стоит посмотреть')
# else:
#     print('этот фильм не стоит смотреть')


# import random
# pc=random.randint(1,10)
# my=int(input('угадайте число от 1 до 10: '))
# if my==pc:
#     print('ты угадал, поздравляю!')
# elif my-1==pc or my+1==pc:
#     print('ты был рядом')
# else:
#     print('ты не угадал')

# temp=int(input('Введите температуру на улице в данный момент: '))
# if temp>=30:
#     print('очень жарко')
# elif 30>=temp>20:
#     print('жарко')
# elif 20>=temp>15:
#     print('тепло')
# elif 15>=temp>8:
#     print('прохладно')
# elif 8>=temp>0:
#     print('холодно')
# else:
#     print('очень холодно')

# import random
# value=['орёл', 'решка']
# pc=random.choice(value)
# my=input('орёл или решка? ')
# if pc==my:
#     print('ты победил')
# else:
#     print('ты проиграл')


# -----РУЧНАЯ СОРТИРОВКА-----

# list_=[-1, 20, 32, -27, 9]
# N=len(list_)
# for i in range(N-1):
#     for k in range(N-1-i):
#         if list_[k]>list_[k+1]:
#             list_[k], list_[k+1] = list_[k+1], list_[k]
# print(list_)

# -----СЛОВАРИ-----

# a={
#     'молоко': 65,
#     'кефир': 70,
#     'список': [12,242,231,5],
#     'словарь': {
#         'ключ': 'значение'
#     }
# }
# print(a['словарь']['ключ'])
# print(a.get('чипсы', 'такого ключа нет'))

# english_dict = {
#     'яблоко':'apple',
#     'молоко':'milk',
#     'кот':'cat'
# }
# word = input('Введите слово на русском языке ')
# if word in english_dict:
#     print(word + ' на английском языке будет: ' + english_dict[word])
# else:
#     print('такого слова нет в словаре')


# -----ФИЛЬМЫ-----

# films_dict = {
#     'Начало':'Леонардо Ди Каприо',
#     'Человек паук':'Том Холанд',
#     'Терминатор':'Арнольд Шварцнеггер',
#     'Драйв':'Райан Гослинг'
# }
# favorite_actor = 'Райан Гослинг'
# film = input('Ведите фильм, который хотите посмотреть: ')
# if film in films_dict:
#     actor = films_dict[film]
#     if actor == favorite_actor:
#         print('Да, этот фильм стоит посмотреть!')
#     else:
#         print('Нет, этот фильм не стоит смотреть!')
# else:
#     print('Такого фильма нет в базе(')


# -----ВОПРОСИКИ ОТВЕТИКИ-----

# qlist =[
#     {
#         'q': 'сколько будет 2+2?',
#         'a': [4,3,5],
#         'r_a': 1
#     },
#     {
#         'q': 'сколько будет 3+4?',
#         'a': [6,8,7],
#         'r_a': 3
#     },
#     {
#         'q': 'сколько будет 9+4?',
#         'a': [14,13,15],
#         'r_a': 2
#     }
#
# ]
# print('Пройди тест, если наберёшь 3 балла, то станешь лучшим программистом!!!')
# print('--------------------------')
# score=0
# name=input('Введите имя: ')
# for que in qlist:
#     print(que['q'])
#     ans_num = 0
#     for ans in que['a']:
#         ans_num += 1
#         print(ans_num,'. ', ans)
#     user_ans=int(input('Введите номер правильного ответа: '))
#     if user_ans == que['r_a']:
#         print('верно!')
#         score+=1
#     else:
#         print('неверно!')
#     print('-----------------------')
#     print(' ')
# if score==3:
#     print('Поздравляю, ты набрал 3 балла и выйграл!')
# else:
#     print('К сожалению, ты проиграл, набрав ', score, ' из 3 баллов(')
#
# file=open('result.txt','a')
# file.write(name + ': ' + str(score) + '\n')
# file.close()
#
# fileR = open('result.txt', 'r')
# print(fileR.read())


# --------------------------------------------------------------

# -----ПЕСНИ-----


# songs={
#     'Sun':2.41,
#     'Нэнси Дрю':3.53,
#     'Blind':2.45,
#     'Glue':4.29
# }
# user = int(input('Сколько песен выбрать? '))
# if user > 4:
#     print('В списке нет столько песен, выбрано максимально возможное число песен-4')
#     user=4
# num = 0
# dur = 0
# for s in range(user):
#     num += 1
#     user_s = input('Введите название песни ')
#     if user_s in songs:
#         dur += songs[user_s]
#     else:
#         print('Такой песни в списке нет(')
# print('Общее время звучания песен: ', dur, ' мин')

# -----ПРОДУКТЫ-----

# codes={
#     'Морковка': '01',
#     'Картофель': '02',
#     'Укроп': '03',
#     'Мука': '04',
# }
#
# store={
#     '01': [
#         {'quant':36 ,'price':40 },
#     ],
#     '02': [
#         {'quant':20,'price':55 },
#         {'quant':23,'price':54 },
#     ],
#     '03': [
#         {'quant':89 ,'price':4 },
#         {'quant':97,'price':3 },
#     ],
#     '04': [
#         {'quant':4 ,'price':103 },
#         {'quant':3,'price':106 },
#         {'quant':7,'price':46 },
#     ],
# }
#
# for item in codes:
#     item_name=item
#     id=codes[item]
#     item_q=0
#     item_p=0
#     for i in store[id]:
#         item_q=i['quant']
#         item_p=i['price'] * item_q
#         print(item_name, '- количество',item_q, ',', 'стоимость', item_p, 'рубля')

# -----------------ФАЙЛЫ----------------
# w-write
# r-read
# a-add
# \n-строка
#
# file = open('result.txt', 'r')
# s=file.readline()
# print(s)
# ---
# file = open('result.txt', 'r')
# for line in file.readlines():
#     print(line)
# ---
# file = open('result.txt', 'r')
# a=[]
# for line in file.readlines():
#     a.append(line)
# print(a)


# -------ФУНКЦИИ-------

# def summ(a):
#     return a+5
#
# result = summ(4)
# print(result)

# def cal(a, b, c):
#
#     if c == '+':
#         result = a+b
#     elif c == '-':
#         result = a-b
#     elif c == '*':
#         result = a*b
#     elif c == '/':
#         result = a/b
#     else:
#         result = 'Такой операции у меня нет'
#     file = open('cal.txt', 'a')
#     file.write(str(result)+'\n')
#     file.close()
#     return result
#
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# c = input('Введите операцию (+ - * /): ')
#
# print(cal(a, b, c))

# СМЕНА МЕСТА МАКСИМАЛЬНОГО И МИНИМАЛЬНОГО

# dogs_score=[23, 1, 75, 76, 21, 22, 100]
# min_score_index=dogs_score.index(min(dogs_score))
# max_score_index=dogs_score.index(max(dogs_score))
#
# min_score_name=dogs_score[min_score_index]
# max_score_name=dogs_score[max_score_index]
#
# dogs_score.insert(min_score_index, max_score_name)
# del[dogs_score[min_score_index + 1]]
# dogs_score.insert(max_score_index, min_score_name)
# del[dogs_score[max_score_index + 1]]
#
# print(dogs_score)


# -------WHILE-------

# i = 0
# while i<10:
#     print(i)
#     i += 1


# a = 0
# s = 0
# while a != -1:
#     s += a
#     a = int(input())
# print(s)

# password = ''
# while password != 'privetcurator235':
#     password = input('Введите пароль: ')
#     if password != 'privetcurator235':
#         print('Неверный пароль')
#     else:
#         print('Всё верно, входите')

# number = int(input('Введите число: '))
# summ = 0
# while number != 0:
#     summ += number
#     number = int(input('Введите число: '))
# print(summ)

# animal = 'Заяц'
# number = 6
# print(f'{animal} спит, {number} число')


# from tkinter import *
#
# window = Tk()
# window.geometry('800x600')
#
# canvas = Canvas(window, width=700, height=500, bg='white' )
# canvas.pack()
#
# # canvas.create_rectangle(10, 10, 30, 30, fill='black', outline='purple', width=3)
# # canvas.create_rectangle(40, 40, 80, 80, fill='black', outline='green', width=3)
# # canvas.create_rectangle(90, 90, 150, 150, fill='black', outline='red', width=3)
# #
# # canvas.create_polygon(130, 240, 190, 160, 250, 240, fill='black', outline='yellow', width=3)
#
# canvas.create_rectangle(90, 90, 150, 150, fill='black', outline='red', width=3)
# canvas.create_polygon(80, 90, 120, 30, 160, 90, fill='black', outline='yellow', width=3)
#
#

#window.mainloop()




#---------------------------------------------

#Тернарный оператор if

# age = 19
# is_allow = False
#
# if age >= 18:
#     is_allow = True
# else:
#     is_allow = False
#
# print(is_allow)

#=====

# age = 19
# is_allow = age >= 18
#
# print(is_allow)

########################

# value = None
# if value is None:
#     res = []
# else:
#     res = value
#
# print(res)

#=====

# value = None
# res = [] if value is None else value
#
# print(res)

#=====

# value = None
# res = value or []
# print(res)

#--------------------------------------------

#Генератор списков

# div_5_list = []
# for x in range(100):
#     if x % 5 == 0:
#         div_5_list.append(x)
# print(div_5_list)

#=====

# div_5_list = [x for x in range(100) if x % 5 == 0]
# print(div_5_list)

#
# list = [x for x in range(251) if (x % 30 == 0 or x % 31 == 0)]
# print(list)


#---------------------------------------------

#Генератор словарей

#some_dict = {'key': 'value'}

# words = ['red', 'orange', 'yellow']
# some_dict = {x: len(x) for x in words}
# print(some_dict)

#=====

# def y(x):
#     return x**2 + 1
#
# some_list = [54151, 516721, 8971, 24, 671]
# some_dict = {x: y(x) for x in some_list}
# print(some_dict)

#------------------------------------------------

# Кортежи

# some_tuple = (1, 2, 3, 4)
# print(some_tuple)

# some_dict = {(1, 2, 3): 'value'}
# print(some_dict)

# some_tuple = (1, 2, 3, 4)
# print(some_tuple)
# some_list = list(some_tuple)
# print(some_list)
# some_list.append(15)
# print(some_list)
# some_tuple = tuple(some_list)
# print(some_tuple)

#----------------------------------------------

# *args **kwargs

# def func(a, b, *args, **kwargs):
#     print(a, b)
#     print(args)
#     print(kwargs)
#
# func(21, 1, one=1, two=2)

#-----------------------------------------------





# numbers = [12, 161, 16778, 1617, 1899, 2, 8]
# chet_list = [x for x in numbers if x % 2 == 0]
# nechet_list = [x for x in numbers if x % 2 != 0]
# print(chet_list, nechet_list)


# some_tuple = (5, 3, 2, 1, 4)
# print(tuple(sorted(list(some_tuple))))

#-----------------------------------------------
#-----------------------------------------------


goods = [
    {
        'name' : 'Iphone 14',
        'brand' : 'Apple',
        'price' : 1200
    },
{
        'name' : 'Iphone XR',
        'brand' : 'Apple',
        'price' : 800
    },
{
        'name' : 'Samsung Galaxy A23',
        'brand' : 'Samsung',
        'price' : 600
    },
{
        'name' : 'Xiaomi Mi 13 Ultra',
        'brand' : 'Xiaomi',
        'price' : 1000
    }
]

# ---------SORTED KEY---------

# def item_price(item): # Замена лямбда функцией
#     return item['price']


# print(sorted(goods, key=lambda item: item['price']))

# ---------FILTER---------

# apple_list = filter(lambda item: item['brand'] == 'Apple', goods)

# for i in apple_list:
#     print(i)
# # ИЛИ
# print(list(apple_list))

# ---------MAP---------

# listofstr = ['1', '2', '3', '4', '5']
# listofint = list(map(int, listofstr))
# print(listofstr, listofint)


# print(list(map(lambda item: item + 'sss', listofstr)))

# ---------ENUMERATE---------

# for index, item in enumerate(goods):
#     print(index, item)

# ---------ZIP---------

# for item in zip([x['name'] for x in goods], [x['price'] for x in goods]):
#     print(item)

# a = [1, 2, 3]
# b = ['1', '2', '3']
# c = ['*', '!', '^']
#
# for item in zip(a, b, c):
#     print(item)

#---------------------


# class Goods:
#     def __init__(self, name, brand, price):
#         self.name = name
#         self.brand = brand
#         self.price = price
#
# item1 = Goods('Iphone XR', 'Apple', 800)
# item2 = Goods('Iphone 14', 'Apple', 1200)
# item3 = Goods('Poco X3 NFC', 'Xiaomi', 350)
#
# goods_list = [item1, item2, item3]
#
# brand_sort_list = list(filter(lambda item: item.brand == 'Apple', goods_list))
#
# print([[x.name, x.brand, x.price] for x in brand_sort_list])




# names_list = ['данил', 'артём', 'никита', 'влад']
#
# names_list = list(map(lambda name: name.capitalize(), names_list))
#
# print(names_list)

#------------------------------------------
#
#
# import sqlite3
#
# class User:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#
#
# def create_table_user(cursor):
#     command = """
#     CREATE TABLE IF NOT EXISTS user (
#         id INTEGER PRIMARY KEY,
#         name TEXT,
#         surname TEXT,
#         gender TEXT)
#     """
#
#     cursor.execute(command)
#
# def add_user(cursor, user):
#     command = """
#         INSERT INTO user(name, surname, gender)
#         VALUES(?, ?, ?)
#     """
#     cursor.execute(command, (user.name, user.surname, user.gender))
#
# def get_users_list(cursor):
#     command = """
#         SELECT * FROM user
#     """
#
#     result = cursor.execute(command)
#     users = list(result)
#     print(users)
#
# def update_user_name(cursor, value, user_id):
#     command = """
#         UPDATE user
#         SET name = ?
#         WHERE id = ?
#     """
#     cursor.execute(command, (value, user_id))
#
#
# def delete_users(cursor):
#     command = """
#             DELETE FROM user
#         """
#     cursor.execute(command)
#
#
#
# with sqlite3.connect('data.db') as cursor:
#     create_table_user(cursor)
#     get_users_list(cursor)
#     update_user_name(cursor, 'Nikita', 1)
#     get_users_list(cursor)
#     delete_users(cursor)
#     get_users_list(cursor)
#     add_user(cursor, User("Ivan", "Ivanov", "male"))
#     add_user(cursor, User("Petr", "Ivanov", "female"))
#
#
#

