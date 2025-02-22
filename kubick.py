# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.
# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.
import matplotlib.pyplot as plt
import random

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
streak = 1 #используем для подсчета текущей длины последовательности одинаковых бросков. Начинаем с 1, так как первый бросок уже произошел.
q = 0 # последний бросок кубика
streaks = []

for _ in range(1000):
    previous_q = q
    q = random.randint(1, 9)

    if q == 1:
        count1 += 1
    elif q == 2:
        count2 += 1
    elif q == 3:
        count3 += 1
    elif q == 4:
        count4 += 1
    elif q == 5:
        count5 += 1
    elif q == 6:
        count6 += 1
    elif q == 7:
        count7 += 1
    elif q == 8:
        count8 +=1
    else:
        count9 += 1

    if previous_q == q:
        streak += 1
    else:
        streaks.append(streak)
        streak = 1

# Добавляем последовательно streak в streaks
streaks.append(streak)

max_streak_length = max(streaks)

results = [count1, count2, count3, count4, count5, count6, count7 , count8 , count9 , max_streak_length]
labels = ['единицы', 'двойки', 'тройки', 'четвёрки', 'пятёрки', 'шестёрки', 'семёрки', 'восьмерки', 'девяткки', 'макс. подряд']
plt.bar(labels, results, color='green')
plt.title('1000 бросков кубика')
plt.show()