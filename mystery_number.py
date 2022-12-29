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
    return_table =[]
    win = 0
    counter = 0
    fail_counter = False
    while win == 0 & fail_counter != True:
        user_number = 0
        number_min: int = 1
        number_max: int = 100
        random_number = random.randint(number_min, number_max)
        while user_number != random_number | fail_counter != True | win != -1:
            user_number = input(f"Entrez un nombre entre {number_min} et {number_max}\n")
            if user_number == 0:
                win = -1
                break
            user_number = int(user_number)
            if user_number == random_number:
                counter +=1
                win = 1
                break
            if user_number > random_number:
                print('Trop grand')
            if user_number < random_number:
                print('trop petit')
            counter += 1
            if counter > 5:
                fail_counter = True
                win = -1
            print(counter)
    return_table.append(win)
    return_table.append(counter)
    return return_table


def replay():
    answer = 0
    while answer != 1 and answer != 2:
        answer = int(input(
            '''voulez vous rejouer ?
            [1] - Yes, let's go !
            [2] - No, Exit please\n'''))
    return answer


def main():
    user_choice = int(display_menu())
    if user_choice == 1:
        return_table = mystery_number()
        if return_table[0] == 1:
            print(f"You won with {return_table[1]} attempts")
            choice_replay = replay()
            while choice_replay == 1:
                if int(choice_replay) == 1:
                    mystery_number()
                    choice_replay = replay()
            else:
                print("Au revoir et à bientôt")
                exit()
        elif return_table[0] == -1:
            print(f"You loose with {return_table[1]} attempts")
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
