# EASY

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

# def circle(i, digits):
#     i = str(i)
#     a = i.find('.')
#     number = i[:a + digits + 1]
#     last_digit = int(number[a + digits])
#     if int(i[a + digits + 1]) >= 5:
#         last_digit += 1
#         number = number[:-1] + str(last_digit)
#
#     return number, type(number)
#
#
# print(circle(450.9254293490, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

# def lucky(a):
#     a = str(a)
#
#     first = 0
#     for i in a[:3]:
#         first += int(i)
#
#     second = 0
#     for i in a[3:]:
#         second += int(i)
#
#     if first == second:
#         return 'Lucky'
#     else:
#         return 'Next time'
#
# print(lucky(456456))

# #NORMAL
#
# # Задание-1:
# # Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# # Первыми элементами ряда считать цифры 1 1
#
# def fibo(n, m):
#     fibonachi = [1, 1]
#     a = 1
#     b = 1
#     last_number = 2
#
#     while last_number != m:
#         last_number += 1
#         a, b = b, a + b
#         fibonachi.append(b)
#     print(fibonachi[n - 1 : m + 1])
#
# fibo(4, 20)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_manual(list):
    n = len(list)
    sorted_list = list
    biggest = 0
    for i in list:
        if int(i) > biggest:
            biggest = int(i)
            sorted_list.append(biggest)
            sorted_list.remove(i)
    print(sorted_list)

sort_manual([23, 1, 45, 8, 12, 3, 456])