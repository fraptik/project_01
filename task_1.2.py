# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

import random
import datetime



my_favorite_songs = [
     ['Waste a Moment', 3.03],
     ['New Salvation', 4.02],
     ['Staying\' Alive', 3.40],
     ['Out of Touch', 3.03],
     ['A Sorta Fairytale', 5.28],
     ['Easy', 4.15],
     ['Beautiful Day', 4.04],
     ['Nowhere to Run', 2.58],
     ['In This World', 4.02],
     ]
time=0
my_favorite_songs_new = []
for i in my_favorite_songs:
    my_favorite_songs_new = random.sample(my_favorite_songs,3) # Пункт С для списка
    time = sum(j[1] for j in my_favorite_songs_new)
sec = int((time - int(time))*100)
min = int(time)
if sec < 60:
     print(f'А)Три песни звучат {int(time)} минут')
else: (min := min + 1) and  print(f'А)Три песни звучат {min} минут')



# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
      'Waste a Moment': 3.03,
      'New Salvation': 4.02,
      'Staying\' Alive': 3.40,
      'Out of Touch': 3.03,
      'A Sorta Fairytale': 5.28,
      'Easy': 4.15,
      'Beautiful Day': 4.04,
      'Nowhere to Run': 2.58,
      'In This World': 4.02,
  }
time1 = 0
my_favorite_songs_dict_new = random.sample(list(my_favorite_songs_dict.items()), 3) # Пункт С для словаря
for i in my_favorite_songs_dict_new:
    time1 += i[1]
sec1 = int((time1 - int(time1))*100)
min1 = int(time1)
if sec1 < 60:
     print(f'В)Три песни звучат {int(time1)} минут')
else: (min1 := min1 + 1) and  print(f'А)Три песни звучат {min1} минут')


# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Для пункта А
m = [j[0] for j in my_favorite_songs_new]

print('A.C) Случайные песни из списка:', m)


# Для пункта B

d = [j[0] for j in my_favorite_songs_dict_new]
print('A.B) Случайные песни из словаря:', d)


# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

# Для пункта А

mt = int(time)
st = round(int((time - int(time))*100),2)
if st <= 59:
    print('D.A) Случайные песни из списка звучат:', datetime.time(0,mt,st).strftime('%M:%S'))
else: (st := st - 60) and (mt := mt + 1) and print('D.A) Случайные песни из списка звучат:', datetime.time(0,mt,st).strftime('%M:%S'))

# Для пункта B

st1 = int((time1 - int(time1))*100)
mt1 = int(time1)
if st1 <= 59:
     print('D.B) Случайные песни из списка звучат:', datetime.time(0,mt1,st1).strftime('%M:%S'))
else: (st1:= st1 - 60) and (mt1:=mt1+1) and  print('D.B) Случайные песни из списка звучат:', datetime.time(0,mt1,st1).strftime('%M:%S'))