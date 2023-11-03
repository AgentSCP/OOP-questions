class Unknown:
    def __init__(self , x=0, y=0, z=0, j=0, k=0, l=0):
        self.x = x
        self.y = y
        self.z = z
        self.j = j
        self.k = k
        self.l = l

    def info(self):
        print(f'x = {self.x}, y = {self.y}, z = {self.z}, j = {self.j}, k = {self.k}, l = {self.l}')

    def first_pre_check(self, a, b, c):
        return a + b + c

    def second_pre_check(self, a, b, c):
        return a + b + c

    def first_check(self):
        return f'Периметр треугольника первых параметров: {self.first_pre_check(self.x, self.y, self.z)}'

    def second_check(self):
        return f'Периметр треугольника вторых параметров: {self.second_pre_check(self.j, self.k, self.l)}'


check = Unknown(2,6,6, 4, 9, 0)
check.info()
print(check.first_check())
print(check.second_check())