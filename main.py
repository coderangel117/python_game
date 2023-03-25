import user_manager
from mystery_number import mystery_number
from utils import check_special_characters


#   @TODO Permit to play in another languages (fr and en)
#   @TODO Add a game menu to select which game the user wants to play
#   @TODO Add different level ( easy, normal, hard)
#   @TODO Add a great score list per game ( the same for fails and wins )
#   @TODO Display the number of laps remaining before failure
#   @TODO Add a menu to choose his player
# Possible games list = ["Pendu", "Roulette", "bingo", "Rock, papern scissors", "Tic-Tac-Toe", "snake"]


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


def games_menu():
    """
        Display games menu and user choose between games or return to main_menu
        :return: int
        """
    manage_choice = 0
    while manage_choice != 1 and manage_choice != 2:
        manage_choice = input('''
            [1] - Mystery number
            [2] - return to main menu
            ''')
        if not check_special_characters(manage_choice):
            manage_choice = 0
        manage_choice = int(manage_choice)
    if manage_choice == 1:
        result = mystery_number()
        check_win(result)
    if manage_choice == 2:
        return "main"
    return manage_choice


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
    # games_menu()


def main():
    user_choice = int(main_menu())
    if user_choice == 1:
        result = games_menu()
        while result != "main":
            result = games_menu()
        main()
    elif user_choice == 2:
        choice = user_manager.users_menu()
        while choice != "main":
            choice = user_manager.users_menu()
        main()
    else:
        print("Bye")
        exit()


if __name__ == '__main__':
    main()
