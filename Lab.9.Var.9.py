#Об’єкт “Площина ”
#поля
# ▪ для зберігання рівняння площини;
#методи
# ▪ введення та виведення коефіцієнтів рівняння площини;
#▪ перевірка належності точки площині;
#▪ встановлення паралельності з іншою площиною.
class Plane:
    def __init__(self,A,B,C,D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
    def __str__(self):
        return f"{self.A}x+{self.B}y+{self.C}z+{self.D}"

    def input_and_output_of_coefficients(self):
        print("Введіть коефіціенти рівняння площини")
        self.A = float(input("A="))
        self.B = float(input("B="))
        self.C = float(input("C="))
        self.D = float(input("D="))
        return f"A:{self.A},B:{self.B},C:{self.C},D:{self.D}"

    def point(self):
        print("Введіть координати")
        self.x = float(input("x="))
        self.y = float(input("y="))
        self.z = float(input("z="))
        if self.x>=0 and self.y>=0 and self.z>=0:
            print("Дана точка належить площині")
        else:
            print("Дана точка не належить площині")


    def parallel(self):
        print("Введіть коефіціенти рівняння прямої на площині")
        self.a= float(input("a="))
        self.b= float(input("b="))
        self.c = float(input("c="))
        self.d= float(input("d="))
        self.e = float(input("e="))
        self.p = float(input("p="))
        if self.a/self.d == self.b/self.e:
            print("Площина паралельна іншій площині")
        else:
            print("Площина не паралельна іншій площині")
plane = Plane(3,5,7,9)
print(plane)
print(plane.input_and_output_of_coefficients())
print(plane.point())
print(plane.plane_parallelism())
# Об’єкт “Аудіо файл”
# поля
# ▪ формат файлу;
# дата створення;
# тривалість;
# частота дискретизації;
# глибина кодування;
# mетоди
# ▪ визначення «віку» файлу;
# визначення кількості точок збереження за вказаний проміжок часу;
# визначення об’єму файлу з вказаною тривалістю.
from datetime import date, time

import self as self


class Audio_file:
    def __init__(self, file_format, date_of_creation, duration, sampling_frequency, coding_depth):
        self.file_format = file_format
        self.date_of_creation = date_of_creation
        self.duration = duration
        self.sampling_frequency = sampling_frequency
        self.coding_depth = coding_depth

    def __str__(self):
        return f"Audio_file:\n File_format:{self.file_format} \n Date_of_creation:{self.date_of_creation} \n Duration:{self.duration}\n Sampling_frequency:{self.sampling_frequency}\n Coding_depth:{self.coding_depth}"

    def file_age(self):
        days = (date(2020, 12, 10) - self.date_of_creation).days
        print("Сьогоднішня дата = 2020-12-10")
        return f"Вік файлу = {days} днів"

    def number_of_save_points(self):
        point = (self.size / (self.coding_depth * self.time))
        print("Проміжок часу = 15,0,0")
        return f" Кількість точок збереження = {point}"

    def size(self):
        self.size = int(input())
        print()
    def size(self):
        self.time = int(input())
        print()
    def file_size(self):
        size = (self.sampling_frequency * self.coding_depth * self.time)
        print("Тривалість аудіофалу = 10.0.0")
        return f"Об’єм файлу = {size}"


file = Audio_file("MP3", date(2020, 12, 12), time(0, 29, 0), 444,15)
print(file)
print(file.file_age())
print(file.number_of_save_points())
print(file.file_size())
