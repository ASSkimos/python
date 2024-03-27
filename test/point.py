import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    @property
    def quarter(self):
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        else:
            return 0

# Пример использования класса
p1 = Point(3, 4)
p2 = Point(5, 5)
print(p1 == p2)  # Выведет False
print(p1.distance_to(p2))  # Выведет 2.8284271247461903
print(p1.quarter)  # Выведет 1