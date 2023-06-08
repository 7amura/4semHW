# Задача No33. Решение в группах
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1

marks = [1, 4, 3 ,3 ,4]
min_m = min(marks)
max_m = max(marks)
for n in range(len(marks)):
    if marks[n] == max_m:
        marks[n] = min_m
          
# marks2 = [min if i == max else i for i in marks]
print(marks)

