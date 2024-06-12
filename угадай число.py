import random


def easy():
    global user_number, pc_number
    attempts = 10
    attempts -= 1

    while attempts > 0:
        attempts -= 1

        if user_number == pc_number:
            print("вы угадали число!")
            break
        elif user_number > pc_number:
            print(f"ваше число больше,попробуйте снова! у вас осталось {attempts + 1} попыток")
            user_number = int(input("угадайте число"))
        elif user_number < pc_number:
            print(f"ваше число меньше попробуйте снова! у вас осталось {attempts + 1} попыток")
            user_number = int(input("угадайте число"))
        if attempts == 0:
            print(f"попытки закончились! было загадано число {pc_number}")


def hard():
    global user_number, pc_number
    attempts = 5
    attempts -= 1

    while attempts > 0:
        attempts -= 1

        if user_number == pc_number:
            print("вы угадали число!")
            break
        elif user_number > pc_number:
            print("ваше число больше,попробуйте снова!")
            user_number = int(input("угадайте число"))
        elif user_number < pc_number:
            print("ваше число меньше попробуйте снова!")
            user_number = int(input("угадайте число"))
        if attempts == 0:
            print(f"попытки закончились! было загадано число {pc_number}")


pc_number = random.randint(1, 100)
level_change = input("выберете уровень сложности: Сложно/Легко").lower()
user_number = int(input("угадайте число"))
if level_change == "легко":
    easy()
elif level_change == "сложно":
    hard()
else:
    print("такого уровня сложности нет,возможно вы допустили какую то ошибку!")
