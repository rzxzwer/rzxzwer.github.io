flights = [
    ['Москва - Питер', 41, '22.08.2005', '14000 rub'],
    ['Москва - Дубай', 0, '29.08.2005', '40000 rub'],
    ['-', 29, '01.09.2005', '25000 rub']
]

while True:
    # Вывод информации о доступных рейсах
    print("Добро пожаловать в приложение 'Бронирование билетов на самолет'!")
    print("Доступные рейсы:")
    for flight in flights:
        print(flight[0], end=" свободные места: ")
        print(flight[1])

    # Запрос на выбор рейса
    chosen_flight = input("Выберите рейс из списка: ")
    while not any(chosen_flight in flight for flight in flights):
        print("Такого рейса нет в списке!")
        chosen_flight = input("Выберите рейс из списка: ")

    # Поиск выбранного рейса
    selected_flight = None
    for flight in flights:
        if chosen_flight in flight:
            selected_flight = flight
            break

    # Проверка наличия свободных мест
    if selected_flight[1] > 0:
        print("Места на рейсе доступны. Вы можете забронировать билет.")
        selected_flight[1] -= 1
        print("Билет успешно забронирован!")
    else:
        print("На выбранный рейс нет доступных мест.")
        print("Попробуйте выбрать альтернативный рейс или ожидайте освобождения мест.")

    # Вывод информации о бронировании
    print("Информация о бронировании:")
    print(f"Рейс: {selected_flight[0]}")
    print(f"Дата: {selected_flight[2]}")
    print(f"Цена: {selected_flight[3]}")

    # Проверяем, хочет ли пользователь забронировать ещё один билет
    answer = input("Хотите забронировать ещё один билет? (да/нет): ")
    if answer.lower() != 'да':
        break

print("Спасибо за использование нашего сервиса!")
