import math
print("--- Задание 2 ---")
x = float(input("Введите значение аргумента x: "))
eps = float(input("Введите погрешность e (например, 0.001): "))

left_part = math.exp(x)

right_part = 1.0
term = 1.0
n = 1

while abs(term) > eps:
    term *= x / n
    right_part += term
    n += 1

print(f"Левая часть (math.exp): {left_part:.6f}")
print(f"Правая часть (ряд):     {right_part:.6f}")
print(f"Число итераций (n):     {n - 1}\n")