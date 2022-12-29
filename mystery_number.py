import random


# @TODO ==> add project CASINO in notion (with multiples games (chosen in a menu))
# @TODO ==> add project hyrule castle in python in notion (check if possible before)
def display_menu():
    answer = 0
    while answer != 1 and answer != 2:
        answer = int(input('''
        [1] - Start the game   
        [2] - Exit the game
    
        '''))
    return answer


def mystery_number():
    win = 0
    while win != 1:
        user_number = 0
        number_min: int = 1
        number_max: int = 100
        random_number = random.randint(number_min, number_max)
        print('user_number', user_number, 'random_number', random_number)
        while user_number != random_number:
            user_number = input(f"Entrez un nombre entre {number_min} et {number_max}\n")
            print(random_number)
            user_number = int(user_number)
            if user_number == random_number:
                print('user_number', user_number, 'random_number', random_number)
                win = 1
                break
            elif user_number > random_number:
                print('Trop grand')
                user_number = input(f"Entrez un nombre entre {number_min} et {number_max}\n")
            elif user_number < random_number:
                print('trop petit')
                user_number = input(f"Entrez un nombre entre {number_min} et {number_max}\n")
            print("user_number = ", user_number)
    print("win", win)
    return win


def replay():
    answer = 0
    while answer != 1 and answer != 2:
        answer = int(input(
            '''voulez vous rejouer ?
            [1] - Yes, let's go !
            [2] - No, Exit please'''))
    return answer


def main():
    user_choice = int(display_menu())
    if user_choice == 1:
        win = mystery_number()
        if win == 1:
            choice_replay = replay()
            while choice_replay == 1:
                if int(choice_replay) == 1:
                    mystery_number()
                    choice_replay = replay()
            else:
                print("Au revoir et à bientôt")
                exit()
    else:
        print("Au revoir et à bientôt")
        exit()


if __name__ == '__main__':
    main()
