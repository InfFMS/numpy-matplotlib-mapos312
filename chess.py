
# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.
# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.
# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
x = np.array([[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0] ]) #ввел доску
plt.imshow(x, cmap='Greys')
OX= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
plt.xticks(range(8), labels=[f"{OX[i]}" for i in range(8)])
plt.yticks(range(8), labels=[f"{i}" for i in range(0, 8, 1)])

x1 = int(input("координата по Х")) - 1
y1 = 8 - int(input("координата по У"))
#рассматриваю ходы по x и потом в еще одном цикле внутреннем для y
for hod_x in [2, -2]:
    for hod_y in [1, -1]:
        x = x1 + hod_x
        y = y1 + hod_y
        if 0 <= x < 8 and 0 <= y < 8:
            o = plt.Circle((x, y), 0.2, facecolor="red")
            ax.add_patch(o)

#рассматриваю ходы по x и потом в еще одном цикле внутреннем для y
for hod_x in [1, -1]:
    for hod_y in [2, -2]:
        x = x1 + hod_x
        y = y1 + hod_y
        if 0 <= x < 8 and 0 <= y < 8:
            o = plt.Circle((x, y), 0.2, facecolor="red")
            ax.add_patch(o)
kon = plt.Circle((x1, y1), 0.4, facecolor="blue")
ax.add_patch(kon)
plt.show()