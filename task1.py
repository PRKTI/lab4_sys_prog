import math
print("--- Задание 1 ---")
N = int(input("Введите целое число N (> 0): "))
summa = 0.0
for i in range(1, N + 1):
    summa += float(i ** i) 
print(f"Сумма 1^1 + 2^2 + ... + {N}^{N} = {summa}\n")
