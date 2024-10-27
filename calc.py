import tkinter as tk
from tkinter import messagebox

def calculate_sum():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())

        sum_result = num1 + num2 + num3
        result_text.set(f"результат: {sum_result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Пожалуйста введите корректные числа")

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())

        product_result = num1 * num2 * num3
        result_text.set(f"результат: {product_result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Пожалуйста введите корректные числа")

# Создаем основное окно приложения
root = tk.Tk()
root.title("Калькулятор")

# Переменные для хранения значений
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)

# Устанавливаем расположение виджетов
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)

# Метки для полей ввода
label1 = tk.Label(root, text="Число 1:")
label2 = tk.Label(root, text="Число 2:")
label3 = tk.Label(root, text="Число 3:")

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)

# Кнопки для вычисления суммы и произведения
sum_button = tk.Button(root, text="Сложить", command=calculate_sum)
product_button = tk.Button(root, text="Умножить", command=calculate_product)

sum_button.grid(row=4, column=0)
product_button.grid(row=4, column=1)

# Отображение результата
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.grid(row=5, column=0, columnspan=3)

# Запуск основного цикла
root.mainloop()