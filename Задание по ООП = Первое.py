class cube:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def info(self):
        print(f'x = {self.x}, y = {self.y}')


    def First_pre_A_check(self, a):
        return a * a
    def First_pre_B_check(self, b):
        return b * b
    def Second_pre_A_check(self, a):
        return a * 4
    def Second_pre_B_check(self, b):
        return b * 4

    def First_check(self):
        return f'Площадь квадрата используя a: {self.First_pre_A_check(self.x)}, Площадь квадрата используя b: {self.First_pre_B_check(self.y)}'
    def Second_check(self):
        return f'Периметр квадрата используя а: {self.Second_pre_A_check(self.x)}, Периметр квадрата используя b: {self.Second_pre_B_check(self.y)}'


information = cube(10, 5)
information.info()
print(information.First_check())
print(information.Second_check())