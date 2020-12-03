#1.Визначити кількість від’ємних елементів матриці з обома парними індексами.
from random import randint
n = int(input("Кількість рядків:"))
m = int(input("Кількість стовпців:"))
matrix = [[randint(-100, 100) for j in range(m)] for i in range(n)]
print(matrix)
d=0
for i in range(n):
    for j in range(n):
        if i % 2 == 0 and j % 2 ==0:
            if matrix[i][j] < 0:
                d+=1
print(f"Кількість від`ємних елементів матриці з обома парними індексами = {d}")

# 2 .Побудувати квадратну матрицю А, елементи якої задаються формулою:
import math
n = int(input("Кількість рядків ="))
m = int(input("Кількість стовпців ="))
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(n):
        element=1/(i+j+2)
        matrix[i].append(element)
print(matrix)


#3 Дано матрицю A.Звести дану матрицю до верхньої трикутної матриці.
n = int(input())
mat = [[0]*n for i in range(n)]
st, m = 1, 0
mat[n//2][n//2]=n*n
for v in range(n//2):
    for i in range(n-m):
        mat[v][i+v] = st
        st+=1
        #i+=1
for i in mat:
    print(*i)

#4Розмістити елементи діагоналі матриці у порядку зростання.
from random import randint
n = int(input("Кількість рядків і стовпців = "))
matrix = [[randint(-100, 100) for j in range(n)] for i in range(n)]
b = []
for i in range(n):
    for j in range(n):
        if i==j:
            element = matrix[i][j]
            b.append(element)
b.sort()
print(matrix)
for i in range(n):
    for j in range(n):
        if i==j:
            element = b[i]
            matrix[i][j] = element
print(matrix)

