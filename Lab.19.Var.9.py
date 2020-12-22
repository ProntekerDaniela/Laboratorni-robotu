# 1
# Дано текстовий файл, який містить цілі числа.
# Визначити кількість парних елементів.
file = open("data1.txt", "r")
numbers = []
for row in file.readlines():
    numbers.append(int(row))
n = len(numbers)
file.close()

d=0
for i in range(n):
    if i % 2 == 0:
        d+=1
print(f"Кількість парних елементів  = {d}")

# 2
# Довідник студента.
# База даних – розклад руху маршрутних таксі: номер маршруту,
# кінцева зупинка, марка автобуса, час поїздки. Організувати вибір за кінцевою зупинкою.
from datetime import datetime

class Base:
    def __init__(self,route_number ,last_stop ,bus_brand,travel_time):
        self.route_number = route_number
        self.last_stop = last_stop
        self.bus_brand = bus_brand
        self.travel_time = travel_time

    def __str__(self):
        return f"{self.route_number} {self.last_stop} {self.bus_brand} {self.travel_time}"

    def __repr__(self):
        return str(self)

class Bus:
    def __init__(self, file_name):
        self.__list = []
        self.file_name = file_name

    def __repr__(self):
        return self.__list

    def __str__(self):
        return str(self.__list)

    @property
    def count(self):
        return len(self.__list)

    def add(self, base):
        self.__list.append(base)

    def save_to_file(self):
        with open(self.file_name, "w") as file:
            for base in self.__list:
                file.write(
                    f"{base.route_number};{base.last_stop};{base.bus_brand};{base.travel_time};\n")

    def load_from_file(self):
        self.__list.clear()
        with open(self.file_name, "r") as file:
            for row in file:
                route_number, last_stop,bus_brand ,travel_time = row.split(";")
                route_number = int(route_number)
                travel_time = int(travel_time)
                self.__list.append(Base(route_number, last_stop,bus_brand ,travel_time ))

    def find_by_last_stop(self,last_stop):
        for base in self.__list:
            if base.last_stop == last_stop:
                return last_stop
        return None

directory = Base("directory.txt")
directory.load_from_file()
print(directory)
print(directory.find_by_last_stop("вулиця Шевченка"))
