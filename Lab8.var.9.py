#1Використовуючи підпрограму для знаходження коренів квадратного рівняння,
# знайти розв’язок наступної системи рівнянь
def solveSquareEquation(a, b, c):

    def discriminant(a, b, c):
        return b**2-4*a*c

    if discriminant(a, b, c) < 0:
        return []
    else:
        x1 = (-b + discriminant(a, b, c) ** (0.5) ) / (2 * a)
        x2 = (-b - discriminant(a, b, c) ** (0.5) ) / (2 * a)
        return [x1, x2]


a = float(input("a="))
b = 2
c = 7
print(f"{a}x**2+{b}x+{c}=0 має розв'язки {solveSquareEquation(a,b,c)}")

def solveSquareEquation(d, e, f):

    def discriminant(d, e, f):
        return e**2-4*d*f

    if discriminant(d, e, f) < 0:
        return []
    else:
        x3 = (-e + discriminant(d, e, f) ** (0.5) ) / (2 * d)
        x4 = (-e - discriminant(d, e, f) ** (0.5) ) / (2 * d)
        return [x3, x4]


d = float(input("d="))
e = -5
f = 2
print(f"{d}x**2+{e}x+{f}=0 має розв'язки {solveSquareEquation(d,e,f)}")

#2Дано послідовність натуральних числень. Використовуючи
#підпрограму, яка дозволяє встановити, чи є послідовність із чотирьох чисел
#арифметичною прогресією, знайти кількість послідовно розміщених четвірок чисел,
#які утворюють арифметичну прогресію.
def progresive(number):
    if a(n)=(a(n-1)+a(n+1))/2:
        res = arithmetic progresive()
    else:
        return progresive(number)
n = int(input("n="))

#3
import random


def x(i):
    if i == 0:
        return 0
    elif i == 1:
        return 7
    else:
        return (x(i-1)*(1+x(i-2)))


n = int(input("n="))
print(f"x{n}={x(n)}")


