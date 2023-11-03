class CPerson:
    gender = 'Мужчина/Men'

    def __init__(self, x, y, z, f, g, h):
        self.x = x
        self.y = y
        self.z = z
        self.f = f
        self.g = g
        self.h = h
        """
        Это начало функции
        """
    def change_data(self): # Данный метод меняет все, из перечисленного в задании
        try:
            a = int(input("Что вы хотите изменить? \n1- Фамилия \n2- Имя \n3- Отчество \n4- День рождение \n5 - Месяц рождения \n6 - Год рождения \n7 - Пол \n====================="))
            if a == 1:
                b = input("Какую фамилию вы напишете?  ")
                self.x = b
            elif a == 2:
                b = input("Какое имя вы напишите?  ")
                self.y = b
            elif a == 3:
                b = input("Какое отчество вы напишите?  ")
                self.z = b
            elif a == 4:
                b = int(input("Какой у вас день рождения? (Подсказка: Нужно ввести исключительно день)  "))
                if b > 31:
                    print("Вы ввели слишком много. Повторите попытку")
                elif b < 1:
                    print("Вы ввели слишком мало. Повторите попытку")
                else:
                    self.f = b
            elif a == 5:
                b = int(input("Какой у вас месяц рождения?  "))
                if b > 12:
                    print("Вы ввели слишком много. Повторите попытку")
                elif b < 1:
                    print("Вы ввели слишком мало. Повторите попытку")
                else:
                    self.g = b
            elif a == 6:
                b = int(input("Какой у вас год рождение?  "))
                self.h = b
            elif a == 7:
                try:
                    b = int(input("У вас какой пол?\n1- Мужчина/Men\n2- Женщина/Women"))
                    if b == 1:
                        check.gender = "Мужчина/Men"
                    elif b == 2:
                        check.gender = "Женщина/Women"
                    else:
                        print("Некорректное значение. Повторите попытку")
                except ValueError:
                    print("=====================\nВы ввели не цифру. Пожалуйста, повторите попытку")
            else:
                print("Некорректное значение. Повторите попытку")
        except:
            print("=====================\nВы ввели не цифру. Пожалуйста, повторите попытку")

    def info_NSM(self):
        print(f'Фамилия = {self.x}, Имя = {self.y}, Отчество = {self.z}')

    def info_date(self):
        print(f'День рождения = {self.f}, Месяц рождения = {self.g}, Год рождения = {self.h}')
        """
        Это конец функции
        """


check = CPerson("Volkov", "Grigorii", "Sergeevich", 29, 6, 2007)
power = True
while power:
    try:
        i = int(input("===================== \nЧто вы хотите сделать? \n1- Изменение данных \n2- Прочитать данных \n3- Завершить процесс \n====================="))
        if i == 1:
            check.change_data()
        elif i == 2:
            print("Показ данных:")
            check.info_NSM()
            check.info_date()
            print(check.gender)
        elif i == 3:
            print("Конец цикла и кода")
            break
        else:
            print("Некорректное значение. Повторите еще раз")
    except:
        print("Вы ввели не цифру. Повторите еще раз")