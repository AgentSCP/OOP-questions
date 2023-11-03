class Unknown:
    def __init__(self , x=0, y=0):
        self.x = x
        self.y = y

    def info(self):
        print(f'x = {self.x}, y = {self.y}')

    def first_pre_check(self, a, b):
        return 1 / 2 * a * b

    def second_pre_check(self, a, b):
        return (2 * a) + b

    def first_check(self):
        return f'Площадь треугольника: {self.first_pre_check(self.x, self.y)}'

    def second_check(self):
        return f'Периметр треугольника: {self.second_pre_check(self.x, self.y)}'

check = Unknown(3,5)
check.info()
print(check.first_check())
print(check.second_check())