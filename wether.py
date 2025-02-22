# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.
import numpy as np
import matplotlib.pyplot as plt

t = np.random.randint(-10, 36, size=365)

a = np.mean(t)

d = np.sum(t > 25)

# Длина самой длинной последовательности дней с температурой ниже 0
s = ''.join(['1' if x < 0 else '0' for x in t]).split('0')
l = max(len(x) for x in s)

# Линейный график температуры
plt.figure(figsize=(12, 6))
plt.plot(t, label='Температура', color='blue')
plt.axhline(y=0, color='black')
plt.axhline(y=25, color='red')
plt.xlabel('День года')
plt.ylabel('Температура')
plt.grid()

# Гистограмма распределения температуры
plt.figure(figsize=(8, 4))
plt.hist(t, bins=np.arange(-10, 37) - 0.5, color='gray', edgecolor='black')
plt.xlabel('Температура')
plt.ylabel('Количество дней')
plt.xticks(np.arange(-10, 36, 5))
plt.grid()

print('Средняя:', a)
print('дни выше 25:', d)
print('max последовательность дней ниже 0:', l)
plt.show()