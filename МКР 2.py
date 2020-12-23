#1import random,import copy

class Matrix:
    def __init__(self,n,m):

        self.matrix = [[random.randrange(0, 10) for j in range(n)] for i in range(m)]

    def print(self):
        matrix = self.matrix
        for i in range(len(matrix)):
            print(matrix[i])
d = Matrix (2,2)
d.print()
matrix_copy = copy.copy(Matrix)
print(Matrix,matrix)

#4
file = open("data1.txt", "r")
numbers = []
for row in file.readlines():
    numbers.append(int(row))
n = len(numbers)
file.close()
d=0
for i in range(n):
    if i >=1 and i <=3 :
        d+=1
print(f"Кількість елементів,що належать відрізку   = {d}")
