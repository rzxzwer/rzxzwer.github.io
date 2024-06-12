# расчет бюджета
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk, ImageFilter


def get_budget():
    plus = float(plus_entry.get())
    minus = float(minus_entry.get())
    bubget = plus - minus
    budget_label.config(text="Состояние бюджета: {:.2f}".format(bubget))


# создаю окно
root = Tk()
root.geometry("650x600")
root.title("Рассчет бюджета")
root.iconbitmap("C:\\Users\\ToFFi\\Downloads\\Значки\\icons8-valorant-512.ico")
root.resizable(False, False)

# создаю фон приложения
canvas = Canvas(root, width=650, height=600)
canvas.pack()

image = Image.open("C:\\КАРТИНКИ\\градиент.jpg")
image = image.resize((650, 600), )
image = image.filter(ImageFilter.GaussianBlur(radius=200))
background_image = ImageTk.PhotoImage(image)
background_label = canvas.create_image(0, 0, anchor=NW, image=background_image)

# Создание элементов управления
income_plus = tk.Label(root, text="Доходы")
income_plus.place(x=270, y=150)

plus_entry = tk.Entry()
plus_entry.place(x=270, y=175)

income_minus = tk.Label(root, text="Расходы")
income_minus.place(x=270, y=200)

minus_entry = tk.Entry()
minus_entry.place(x=270, y=225)

budget_button = Button(root, text="Рассчитать бюджет", command=get_budget)
budget_button.place(x=270, y=250)

budget_label = tk.Label(root, text="Состояние бюджета: ")
budget_label.place(x=270, y=295)

root.mainloop()
