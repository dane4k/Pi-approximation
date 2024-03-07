import tkinter as tk
import random as rd


def generate_points():
    points_quantity = 1000
    canvas.create_rectangle(50, 50, 250, 250)  # создаем квадрат
    canvas.create_oval(50, 50, 250, 250)  # создаем окружность
    points_inside = 0  # количество точек внутри круга
    points_total = 0  # всего точек

    x1 = [rd.uniform(-1, 1) for _ in range(points_quantity)]
    y1 = [rd.uniform(-1, 1) for _ in range(points_quantity)]
    for i in range(len(x1)):
        x = 150 + x1[i] * 100  # масштабирование координат точек внутри квадрата
        y = 150 + y1[i] * 100
        if (x - 150) ** 2 + (
                y - 150) ** 2 <= 100 ** 2:  # если точка входит в окружность, аналог a^2+b^2 <= 1, только по масштабированным координатам
            color = 'green'  # если внутри, точка зеленого цвета
            points_inside += 1  # количество точек внутри
        else:
            color = 'red'  # если не входит в окружность, точка красного цвета
        canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill=color)
        points_total += 1
    approximation = 4 * (
            points_inside / points_total)  # вычисляет аппроксимацию числа pi = 4 * N1 * Nобщ (по соотношению площадей круга и квадрата)
    print(approximation)
    generate_button.configure(state=tk.DISABLED)  # после одного клика по кнопке она становится некликабельной
    approximation_label.configure(text=str(approximation))  # обновление значения аппроксимации на холсте


def generate_points_button():
    generate_points()


window = tk.Tk()
window.title('Отображение точек')
window.geometry('450x450')

canvas = tk.Canvas(window, width=300, height=300)
canvas.pack()

generate_button = tk.Button(window, text='Сгенерировать точки',
                            command=generate_points_button)  # кнопка с command основная функция
generate_button.pack()

approximation_label = tk.Label(window, text='')  # значение approximation на холсте
approximation_label.pack()

window.mainloop()
