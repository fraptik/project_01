# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

print(my_favorite_songs[0:14],my_favorite_songs[64:77],my_favorite_songs[16:30],my_favorite_songs[51:62]) #Вариант 1

#Вариант 2.

songs_list = my_favorite_songs.split(', ')

print(songs_list[0],songs_list[-1],songs_list[1],songs_list[-2])