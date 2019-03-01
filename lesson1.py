# EASY
# Задача-1

n = input('Введите число:')
a = str(n)
for i in a:
    print(i)

# не понял, как и зачем использовать цикл while в этой задаче.


# Задача-2
num1 = int(input('Введите первое число:'))
num2 = int(input('Введите второе число:'))
a = num1 + num2

num1 = a - num1
num2 = a - num2
print(num1, num2)

# Задача-3
age = input('Введите Ваш возраст:')

if float(age) >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')
# не предусмотрено, если пользователь введет не цифры, а слова, в этом случае перевести во float не получится и выдаст ошибку

# NORMAL
# Задача-1
x = 58375

maximum = []
for i in str(x):
     maximum += i
print(max(maximum))

# снова не понял, как и зачем использовать цикл while в этой задаче.

# Задача-2
num1 = int(input('Введите первое число:'))
num2 = int(input('Введите второе число:'))

num1, num2 = num2, num1
print(num1, num2)

# Задача-3
a = int(input('Введите первый коэффициент уравнения:'))
b = int(input('Введите второй коэффициент уравнения:'))
c = int(input('Введите третий коэффициент уравнения:'))

import math # импорт модуля math

dis = b ** 2 - 4 * a * c
if dis > 0:
    x1 = (- b + math.sqrt(dis)) / 2 * a
    x2 = (- b - math.sqrt(dis)) / 2 * a
    print('X1 =', x1, 'X2 =', x2)
elif dis == 0:
    x = -b / 2 * a
    print('X1 = X2 =', x)
else:
    print('No solution')

# HARD
# Задача-1
a = int(input('Введите число:'))
n = 0
is_complex = 0
while n != a:
    n += 1
    if a % n == 0:
        is_complex += 1

if is_complex > 2:
    print('Число не простое')
else:
    print('Число простое')

# Задание-2

n = int(input('Введите n-ое число Фибоначчи:'))
fibonachi = [0, 1]
a = 0
while n != a:
    a += 1
    i = fibonachi[-1] + fibonachi[-2]
    fibonachi.append(i)

if n == 1:
    print(fibonachi[0])
elif n == 2:
    print(fibonachi[1])
else:
    print(fibonachi[-3])

# Задание-3
n = int(input('Введите количество строк:'))
m = int(input('Введите количество троек ААА:'))
n_string = 0
while n != 0:
    n -= 1
    n_string += 1
    if n_string % 2 == 0:
        print('BBBAAA' * m)
    else:
        print('AAABBB' * m)
