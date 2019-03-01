# Easy

# Задача-1:
fruit_list = ["яблоко", "банан", "киви", "арбуз"]
n = 1
for i in fruit_list:
    print(f'{n}.{i:>10}')
    n +=1

# Задача-2:
first_list = {1, 2, 6, 7, 9, 3, 'dfo', 'rp', 'a', 'h', 'n'}
second_list = {1, 2, 6, 'dfo', 'a', 'h', 'n', 'onf', 34, 90, 'gf'}

clear_list = first_list - first_list.intersection(second_list)
print(clear_list)

# Задача-3:

rand_list = [1, 56, 4, 6, 74, 9, 6, 3, 27]
new_list = []
for i in rand_list:
    if i % 2 == 0:
        new_list.append(i / 4)
    else:
        new_list.append(i * 2.0)
print(new_list)

# Normal

# Задача-1:
old_list = [2, -5, 8, 9, -25, 25, 4, 81, 13]
new_list = []

for i in old_list:
    root = i ** 0.5
    if isinstance(root, float) and float(root) == int(root):
        new_list.append(root)
print(new_list)

#Задача-2:
dates = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое', '06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое', '11': 'одиннадцатое',
         '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое', '16': 'шестнядцатое', '17': 'семнадцатое', '18': 'восемьнадцатое', '19': 'девятнадцатое',
         '20': 'двадцатое', '21': 'двадцать первое', '22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвертое', '25': 'двадцать пятое', '26': 'двадцать шестое',
         '27':'двадцать седьмое', '28': 'двадцать восьмое', '29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое'}

months = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня', '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября',
          '11': 'ноября', '12': 'декабря'}

print_date = input('Введите дату в формате дд.мм.гггг:')

print(f'{dates[print_date[0:2]]} {months[print_date[3:5]]} {print_date[6:10]} года ')

# Задача-3:
import random

n = int(input('Количество символов:'))
list_num = []
while n != 0:
    n -= 1
    list_num.append(random.randint(-100, 100))

print(list_num)

# Hard

# Задача-1:
text = input('Введите текст:')

total = {}
for i in text.split(" "):
    if i not in total:
        total[i] = 1
    else:
        total[i] += 1

all_word = 0
for k in total.values():
    all_word += k

eng_letters = 0
for i in text:
    if ord(i) <= 127 and ord(i) != 32:
        eng_letters += 1

print(all_word)
print(eng_letters)

# Задача-2
first_text = input("Введите первый текст:")
second_text = input("Введите второй текст:")


def make_list(string):
    new_text = []
    for i in string.split(" "):
        new_text.append(i)
    return new_text

new_f_t = (make_list(first_text))
new_s_t = (make_list(second_text))

print(set(new_f_t).intersection(new_s_t))

# EXTRA
recipe = {'яйцо': 4, 'молоко': 0.5, 'помидор': 1, 'лук': 1, 'соль': 5} # омлет
good_list = {'яйцо': 1, 'молоко': 0.3, 'помидор': 1, 'лук': 1, 'соль': 4}
need_to_buy = {}

for i in recipe:
    if recipe[i] > good_list[i]:
        need_to_buy[i] = (recipe[i] - good_list[i])

if need_to_buy == {}:
    print('ничего не нужно')
else:
    print(need_to_buy)