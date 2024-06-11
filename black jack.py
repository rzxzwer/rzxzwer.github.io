import random


def give_cards_first():
    for i in range(2):
        random_card = random.choice(cards)
        dealer_card.append(random_card)
        if i == 0:
            show_dealer_card.append("X")
        else:
            show_dealer_card.append(random_card)
    for i in range(2):
        random_card = random.choice(cards)
        user_card.append(random_card)


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

balance_input = int(input("введите ваш баланс"))
print(f"на балансе {balance_input}")

while balance_input > 0:
    bid_inpunt = int(input("ведите ставку"))
    while bid_inpunt > balance_input:
        print("у вас недостаточно средств!")
        bid_inpunt = int(input("введите ставку"))
    print(f"вы сделали ставку в размере {bid_inpunt}")

    while True:
        dealer_card = []
        show_dealer_card = []
        user_card = []
        give_cards_first()
        sum_user_card = sum(user_card)
        sum_dealer_card = sum(dealer_card)
        print(f"карты дилера: {dealer_card}")
        print(f"карты пользователя: {user_card}")

        if sum_dealer_card and sum_user_card == 21:
            print("ничья")
            print(f"ваши карты: {user_card}, карты диллера: {dealer_card}")
            print(f"ваш баланс: {balance_input}")
            break
        elif sum_user_card == 21:
            print("Блекджек! вы выйграли!")
            print(f"ваши карты: {user_card}, карты диллера: {dealer_card}")
            bid_inpunt *= 2
            balance_input += bid_inpunt
            print(f"ваш баланс: {balance_input}")
            break
        elif sum_dealer_card == 21:
            print("у дилера Блекджек! вы проиграли!")
            print(f"ваши карты: {user_card}, карты диллера: {dealer_card}")
            balance_input -= bid_inpunt
            print(f"ваш баланс: {balance_input}")
            break

        another_card = input("взять еще? да\нет?").lower()

        if another_card == "да":
            random_card = random.choice(cards)
            user_card.append(random_card)
            sum_user_card = sum(user_card)

        if sum_user_card > 21:
            print("Вы проиграли!")
            print(f"ваши карты: {user_card}, карты диллера: {dealer_card}")
            balance_input -= bid_inpunt
            print(f"ваш баланс: {balance_input}")
            break

        while sum_dealer_card < 17:
            random_card = random.choice(cards)
            dealer_card.append(random_card)
            sum_dealer_card = sum(dealer_card)

        if sum_dealer_card > 21:
            print("Вы победили!")
            print(f"ваши карты: {user_card}, карты диллера: {dealer_card}")

            balance_input += bid_inpunt
            print(f"ваш баланс: {balance_input}")
            break
        elif sum_dealer_card == sum_user_card:
            print("Ничья!")
            print(f"ваши карты: {user_card}, карты диллера: {dealer_card}")
            print(f"ваш баланс: {balance_input}")
            break
        elif sum_dealer_card < sum_user_card:
            print("Вы победили!")
            print(f"ваши карты: {user_card}, карты диллера: {dealer_card}")

            balance_input += bid_inpunt
            print(f"ваш баланс: {balance_input}")
            break
        else:
            print("Вы проиграли!")
            print(f"ваши карты: {user_card}, карты диллера: {dealer_card}")
            balance_input -= bid_inpunt
            print(f"ваш баланс: {balance_input}")
            break
