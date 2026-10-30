import math
print("--- Задание 3 ---")
num_str = input("Введите число: ")
even_count = 0

for char in num_str:
    if char.isdigit():       
        digit = int(char)
        if digit % 2 == 0:   
            even_count += 1

print(f"Количество чётных цифр в числе: {even_count}")