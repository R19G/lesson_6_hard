from math import pi


class Figure:

    sides_count = 0
    # При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count,
    # то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
    def __init__(self, color = [0, 0, 0], *sides, filled = False):
        if len(sides) == self.sides_count:
            self.__sides = list(sides)
        elif len(sides) == 1:
            self.__sides = [sides[0] for i in range(self.sides_count)]
        elif len(sides) > self.sides_count or len(sides) < self.sides_count:
            self.__sides = [1 for i in range(self.sides_count)]
        if len(color) == 3:
            self.__color = color
        else:
            print('Попробуй еще раз.')
        self.filled = filled

    # Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных
    # значений перед установкой нового цвета. Корректный цвет: все значения r, g и b - целые числа в диапазоне
    # от 0 до 255 (включительно).
    def __is_valid_color(self, r, g, b):
        list_1 = []
        for number in [r, g, b]:
            if 0 <= number <= 250 and isinstance(number, int):
                list_1.append(True)
            else:
                list_1.append(False)
        if all(list_1):
            return True
        else:
            return False

    # Метод get_color, возвращает список RGB цветов.
    def get_color(self):
        return self.__color

    # Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
    # предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            self.__color = list(self.__color)

    # Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны
    # целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
    def __is_valid_sides(self, *args):
        if len(args) == self.sides_count:
            for i in args:
                if i > 0 and isinstance(i, int):
                    return True
        else:
            return False

    # Метод get_sides должен возвращать значение я атрибута __sides.
    def get_sides(self):
        return list(self.__sides)

    # Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count,
    # то не изменять, в противном случае - менять.
    def set_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            return self.__sides
        else:
            self.__sides = new_sides
            return self.__sides

    # Метод __len__ должен возвращать периметр фигуры.
    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):

    sides_count = 1

    # Все атрибуты и методы класса Figure
    def __init__(self, color = [0, 0, 0], *radius, filled = False):
        super().__init__(color, filled = False)
        # Если в радиус передадим кортеж(список), содержащий одно значение, то в значение радиуса будет передан список,
        # содержащий это значение
        if len(radius) == 1:
            self.__radius = [radius[0] for i in range(self.sides_count)]
        # Если в радиус передадим кортеж(список), который содержит больше или меньше элементов, чем 1, то в значение
        # радиуса будет передан список [1]
        elif len(radius) > self.sides_count or len(radius) < self.sides_count:
            self.__radius = [1 for i in range(self.sides_count)]

    # Переопределяем метод set_sides для того, чтобы можно было изменить радиус окружности и посмотреть, как изменится
    # ее площадь
    def set_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            return self.__radius
        else:
            self.__radius = list(new_sides)
            return self.__radius

    # Переопределяем метод get_sides
    def get_sides(self):
        return list(self.__radius)


    # Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
    def get_square(self):
        # Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
        radius = self.get_sides()[0]
        return pi * radius ** 2

    def __len__(self):
        return sum(self.__radius)

class Triangle(Figure):

    sides_count = 3

    def get_square(self):
        half_per = sum(self.get_sides()) / 2
        return math.sqrt(half_per * (half_per - self.get_sides()[0]) * (half_per - self.get_sides()[1]) *
                         (half_per - self.get_sides()[2]))


class Cube(Figure):

    sides_count = 12

    def __init__(self, color = [0, 0, 0], *sides, filled = False):
        super().__init__(color, filled = False)
        if len(sides) == 1:
            self.__sides = [sides[0] for i in range(self.sides_count)]
        else:
            self.__sides = [1 for i in range(self.sides_count)]

    def get_sides(self):
        return list(self.__sides)

    def get_volume(self):
        return self.__sides[0] ** 3


if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())

