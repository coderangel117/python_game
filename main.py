import user_manager
from mystery_number import mystery_number
from utils import check_special_characters


#   @TODO Permit to play in another languages (fr and en)
#   @TODO Add a game menu to select which game the user wants to play
#   @TODO Add different level ( easy, normal, hard)
#   @TODO Add a great score list per game ( the same for fails and wins )
#   @TODO Display the number of laps remaining before failure
#   @TODO Add a menu to choose his player


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


def games_menu():
    """
        Display users' manager menu
        :return: int
        """
    manage_choice = 0
    while manage_choice != 1 and manage_choice != 2 and manage_choice != 3 and manage_choice != 4 and manage_choice != 5 and manage_choice != 6:
        manage_choice = input('''
            [1] - Mystery number
            [2] - return to main menu
            ''')
        if not check_special_characters(manage_choice):
            manage_choice = 0
        manage_choice = int(manage_choice)
    return manage_choice


def loop_choosegame(choice: int):
    while choice != 0:
        if choice == 1:
            choice = mystery_number()
            return_table = mystery_number()
            check_win(return_table)
            choice_replay = replay_menu()
            loop_replay(choice_replay)
        if choice == 2:
            return "main"


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
        choice = games_menu()
        return_user = loop_choosegame(choice)
        if return_user == 'main':
            main()
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
