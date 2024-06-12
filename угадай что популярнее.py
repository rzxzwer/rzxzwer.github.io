import random
from game_data import data

score = 0
winner = None
winner_displayed = None
a = None
b = None
play_continue = True


def game():
    global a, b, winner, random_dict, random_dict2
    if winner:
        a = (
            f" {winner['name']}, a {winner['description']}, from: {winner['country']}, {winner['follower_count']}")
        random_dict2 = random.choice(data)
        b = (
            f" {random_dict2['name']}, a {random_dict2['description']}, from: {random_dict2['country']}, {random_dict2['follower_count']}")
        if winner['follower_count'] > random_dict2['follower_count']:
            winner = winner
            winner_displayed = winner['name']
        else:
            winner = random_dict2
            winner_displayed = random_dict2['name']
        print(winner_displayed)
        print(f"A:{a}, \nB:{b}")

    else:
        random_dict = random.choice(data)
        a = (
            f" {random_dict['name']}, a {random_dict['description']}, from: {random_dict['country']}, {random_dict['follower_count']}")
        random_dict2 = random.choice(data)
        b = (
            f" {random_dict2['name']}, a {random_dict2['description']}, from: {random_dict2['country']}, {random_dict2['follower_count']}")
        if random_dict['follower_count'] > random_dict2['follower_count']:
            winner = random_dict
            winner_displayed = random_dict['name']
        else:
            winner = random_dict2
            winner_displayed = random_dict2['name']
        print(winner_displayed)
        print(f"A:{a}, \nB:{b}")

    return random_dict, random_dict2, winner_displayed, winner


def choice(winner_displayed):
    global play_continue
    user_choice = input("выберите вариант ответа A or  B ").lower()
    if user_choice == "a" and random_dict['follower_count'] > random_dict2['follower_count']:
        print(f"вы абсолютно правы,побеждает {winner_displayed}")
    elif user_choice == "b" and random_dict['follower_count'] < random_dict2['follower_count']:
        print(f"вы абсолютно правы,побеждает {winner_displayed}")
    elif user_choice == "a" and random_dict['follower_count'] < random_dict2['follower_count']:
        print(f"неверно!! игра окончена! {winner_displayed} имеет больше подписчиков")
        play_continue = False
    elif user_choice == "b" and random_dict['follower_count'] > random_dict2['follower_count']:
        print(f"неверно!! игра окончена! {winner_displayed} имеет больше подписчиков")
        play_continue = False
    return play_continue


while play_continue == True:
    random_dict, random_dict2, winner_displayed, winner = game()
    play_continue = choice(winner_displayed)
