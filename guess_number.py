import random


def main():
    choice = -1
    choice = input(f" Que voulez vous faire\n"
                   f"0 - Quitter\n"
                   f"1 - Jouer\n")
    while choice != '0':
        user_choice = int(choice)
        if user_choice == 1:
            guess_number()
    exit(1)


def guess_number():
    number_min: int = 1
    number_max: int = 100
    foo = random.randint(number_min, number_max)
    print(foo)
    user_number = input(f'Entrez un nombre entre {number_min} et {number_max}\n')
    user_number = int(user_number)
    if user_number == foo:
        print('Congrats')
        exit()
    elif user_number >= number_max or user_number <= number_min:
        print('tou tou fout de ma gueule ?!')
    return number_max


if __name__ == '__main__':
    main()
