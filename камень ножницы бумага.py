# камень ножницы бумага

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# инструменты
list_choise = [rock, paper, scissors]

# выборы обеих сторон
opponent_choise = random.randint(0, 2)
user_choise = int(input("Что ты выбираешь? Введите 0 для камня, 1 для бумаги или 2 для ножниц"))

print(f"вы выбрали\n{list_choise[user_choise]}")
print(f"ваш противник выбрал\n{list_choise[opponent_choise]}")
print("ИТОГ:")

# победа
if user_choise == 0 and opponent_choise == 2 or user_choise == 1 and opponent_choise == 0 or user_choise == 2 and opponent_choise == 1:
    print("вы победили")
# ничья
elif user_choise == opponent_choise:
    print("у вас ничья")
# поражение
else:
    print("вы проиграли")
