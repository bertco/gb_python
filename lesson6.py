# Задача-1:
#
# Создать класс треугольник и реализовать в нем конструктор, методы для вычисления
# (не печати, нужен return) площади, периметра  и вывод значений сторон треугольника на экран.
# В конструкторе сделать проверку на возможность создания такого треугольника, если нет, то написать,
# что такой треугольник нельзя создать и сделать exit(1)

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = float(side1)
        self.side2 = float(side2)
        self.side3 = float(side3)
        if (self.side1 + self.side2) < self.side3 or (self.side1 + self.side3) < self.side2 or (
                self.side2 + self.side3) < self.side1 or self.side1 <= 0 or self.side2 <= 0 or self.side3 <= 0:
            print("Треугольник нельзя создать. Проверь заданные стороны")
            exit()

    def perimetr(self):
        return 1 / 2 * (self.side1 + self.side2 + self.side3)
    def square(self):
        return (self.perimetr() * (self.perimetr() - self.side1) * (self.perimetr() - self.side2) * (self.perimetr() - self.side3)) ** 0.5



triangle1 = Triangle('2', '2', '1')
# triangle2 = Triangle('10', '43', '2')

print(triangle1.perimetr())
# print(triangle2.perimetr())

print(triangle1.square())
# print(triangle2.square())



# Задание-2:
#
# Написать класс, который будет удобно использовать для работы с (на выбор что-нибудь одно)
# комплексными числами \ матрицами \ светофор \ микроволновка

class Lights:
    def __init__(self, color):
        self.color = color

    def action(self):
        if self.color == '1':
            return 'Стой!'
        elif self.color == '2':
            return 'Жди!'
        elif self.color == '3':
            return'Иди!'



color = Lights(input('Какой цвет светофорора:''\n''[1] - красный''\n''[2] - желтый''\n''[3] - зеленый''\n'))
print(color.action())