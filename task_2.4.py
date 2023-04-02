# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"
line = input('Введите строку: ')

def remove_exclamation_marks(s):
    return s.replace('!', '')
print(remove_exclamation_marks(line))

# Пункт B.
# Удалите восклицательный знак из конца строки.
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    for i in range(len(s))[::-1]:
        if s[i] != "!":
            return s[:i + 1]

print(remove_last_em(line))

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    words = s.split()
    new_words = []
    for word in words:
        if word.count('!') != 1:
            new_words.append(word)
    return ' '.join(new_words)
print(remove_word_with_one_em(line))