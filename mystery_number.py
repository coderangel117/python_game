import random
import re

import user_manager


#  @TODO Permit to play in another languages (fr and en)
def check_special_characters(userinput: str):
    regex = re.compile('[@.€ç_!#$%^&*()<>\' \'?\"/\|}{~:A-z]')
    if regex.search(userinput) is not None:
        print("Only number please")
        return False
    elif userinput == "":
        print("Type something ....")
        return False
    else:
        return True


def main_menu():
    """
    Display main menu
    :return: int: return user's answer
    """
    answer = 0
    while answer != 1 and answer != 2 and answer != 3:
        answer = input(
            """
            [1] - Start the game   
            [2] - Manage users
            [3] - Exit the game
            """)
        if not check_special_characters(answer):
            answer = 0
        else:
            answer = int(answer)
    return answer


def replay_menu():
    """
    Display replay menu after game
    :return: int : return user's answer
    """
    answer = 0
    while answer != 1 and answer != 2:
        answer = input(
            '''Would you replay ?
            [1] - Yes, let's go !
            [2] - No, exit please\n''')
        if not check_special_characters(answer):
            answer = 0
        answer = int(answer)
    return answer


def users_menu():
    """
    Display users' manager menu
    :return: int
    """
    manage_choice = 0
    while manage_choice != 1 and manage_choice != 2 and manage_choice != 3 and manage_choice != 4 and manage_choice != 5 and manage_choice != 6:
        manage_choice = input('''
        [1] - Display users list    
        [2] - Search a specific user    
        [3] - Create a new user
        [4] - Update user info
        [5] - Delete a user
        [6] - return to main menu
        ''')
        if not check_special_characters(manage_choice):
            manage_choice = 0
        manage_choice = int(manage_choice)
    return manage_choice


def mystery_number():
    return_table = []
    win = 0  # When user finds the great number
    counter = 0  # The user's attempt count
    force_counter = 0  # Increment when user doesn't respect game's instructions
    fail_counter = False  # Become True when user has exceeded max attempts
    while win == 0 & fail_counter != True:
        user_number = 0
        number_min: int = 1
        number_max: int = 100
        random_number = random.randint(number_min, number_max)
        while user_number != random_number | fail_counter != True | win != -1 | win != -2:
            user_number = input(f"Type a number between {number_min} and {number_max}\n")
            if not check_special_characters(user_number):
                break
            if user_number == "":
                print("Type something ....")
                break
            user_number = int(user_number)
            if user_number == 0 or user_number > number_max or user_number < number_min:
                if force_counter >= 5:
                    win = -2
                    break
                else:
                    print(f"It's between {number_min} and {number_max} ....")
                    force_counter += 1
                    break
            if user_number == random_number:
                counter += 1
                win = 1
                break
            if user_number > random_number:
                print('Your number is bigger than the mystery number')
            if user_number < random_number:
                print('Your number is smaller than the mystery number')
            counter += 1
            if counter > 5:
                fail_counter = True
                win = -1
    return_table.append(win)
    return_table.append(counter)
    return return_table


def check_win(table):
    """
    Check and return true if user wins
    increment nb fail or nbwin user's property if fails or wins
    :param table:
    :return: boolean
    """
    if table[0] == 1:
        print(f"You won with {table[1]} attempts")
        return True
    elif table[0] == -1:
        print('You loose because you doesn\'t find the number before the last attempt')
        return False
    elif table[0] == -2:
        print('You loose because you are a monkey')
        return False


def loop_replay(choice: int):
    while choice != 2 | choice != 0:
        if int(choice) == 1:
            table = mystery_number()
            check_win(table)
            choice = replay_menu()
        else:
            exit()


def main():
    user_choice = int(main_menu())
    if user_choice == 1:
        return_table = mystery_number()
        check_win(return_table)
        choice_replay = replay_menu()
        loop_replay(choice_replay)
    elif user_choice == 2:
        choice = users_menu()
        return_user = user_manager.loop_usermanager(choice)
        if return_user == 'main':
            main()
    else:
        print("Bye")
        exit()


if __name__ == '__main__':
    main()
