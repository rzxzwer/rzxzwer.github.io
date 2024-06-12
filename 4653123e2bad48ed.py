# погода
from tkinter import *
import requests
from PIL import Image, ImageTk, ImageFilter


def get_weather():
    city = entry.get()
    api_key = "a29f1b242da1a5fc7268c8e3090f95ad"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    temperature = round(data["main"]["temp"])
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    country = data["sys"]["country"]

    weather_info = f"Погода в городе {city}:\nТемпература: {temperature}°C\nВлажность: {humidity}%\nСкорость ветра: {wind_speed} м/с\nСтрана: {country}"
    canvas.delete("weather_info")
    canvas.create_text(350, 450, text=weather_info, fill="black", tags="weather_info")

    image2 = Image.open("C:\\КАРТИНКИ\\показ погоды.png")
    image2 = image2.resize((70, 50))
    global background_image1
    background_image1 = ImageTk.PhotoImage(image2)
    background_label1 = canvas.create_image(310, 360, anchor=NW, image=background_image1)


# создаю окно
root = Tk()
root.geometry("700x550")
root.title("Погода today?")
root.iconbitmap("C:\\КАРТИНКИ\\погода.ico")
root.resizable(False, False)

# фон приложения
canvas = Canvas(root, width=700, height=550)
canvas.pack()

image = Image.open("C:\\КАРТИНКИ\\фон погоды.jpg")
image = image.resize((700, 550), )
image = image.filter(ImageFilter.GaussianBlur(radius=3))
background_image = ImageTk.PhotoImage(image)
background_label = canvas.create_image(0, 0, anchor=NW, image=background_image)

image3 = Image.open("C:\\КАРТИНКИ\\облако пнг.png")
image3 = image3.resize((220, 200))
background_image3 = ImageTk.PhotoImage(image3)
background_label3 = canvas.create_image(235, -55, anchor=NW, image=background_image3)
# поля ввода
city_label = canvas.create_text(350, 50, text="Введите название города:", font=("Arial", 8, "bold"), fill="black")
entry_var = StringVar()
entry = Entry(root, textvariable=entry_var)
canvas.create_window(350, 100, window=entry)

get_weather_button = Button(root, text="Получить погоду", command=get_weather)
canvas.create_window(350, 150, window=get_weather_button)

root.mainloop()

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

# Книга рецептов

from tkinter import *
from PIL import Image, ImageTk, ImageFilter


def open_new_window(title, recipe):
    new_window = Toplevel(root)
    new_window.title(title)
    Label(new_window, text=recipe).pack()


def search_recipe():
    search = search_string.get()
    recipe = recipe_dict.get(search, None)

    if recipe is not None:
        open_new_window(search, recipe)
    else:
        recipe_label.config(text='Рецепт не найден')


root = Tk()
root.geometry("700x550")
root.title("Книга рецептов")
root.iconbitmap("C:\\Users\\ToFFi\\Downloads\\Значки\\icons8-pixel-gun-3d-512_1.ico")
root.resizable(False, False)

# Создание фона приложения
canvas = Canvas(root, width=700, height=550)
canvas.pack()

image = Image.open("C:\\КАРТИНКИ\\рецепт.jpg")
image = image.resize((700, 550))
image = image.filter(ImageFilter.GaussianBlur(radius=5))
background_image = ImageTk.PhotoImage(image)
background_label = canvas.create_image(0, 0, anchor=NW, image=background_image)

recipe_dict = {'Борщ': 'Рецепт для борща...', 'Омлет': 'Рецепт для омлета...'}

# Создание поля ввода
search_string = StringVar()
search_entry = Entry(root, textvariable=search_string)
search_entry.place(x=285, y=300)

# Создание кнопки поиска
search_button = Button(root, text="Поиск", command=search_recipe)
search_button.place(x=330, y=330)

# Метка с текстом рецепта
recipe_label = Label(root, text="", bg='white')
recipe_label.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
