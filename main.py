import json

import mystery_number
import rock_paper_scissors
import user_manager
import utils


#   @TODO Permit to play in another languages (fr and en)
#   @TODO Add different level (easy, normal, hard) (default => normal but can be changed)
#   @TODO Add a great score list per game (the same for fails and wins)
# Possible games list = ["Pendu alias hang_man", "Roulette", "bingo", "Tic-Tac-Toe", "snake"]


def choose_player():
    """
        Permit to user to choose with wich profile he wants to play
        :return: str
    """
    users = user_manager.get_user_files()
    user_manager.merge_json_files(users)
    with open('users.json') as users:
        tab = json.load(users)
        if tab:
            i = 1
            for p in tab:
                if p['username'] == 'invite':
                    print(f"{i} - {p['username']} (enter to choose) ")
                else:
                    print(f"{i} - {p['username']}")
                i += 1
        else:
            print("No user found in list... \n"
                  "User invite (default) selected ")
            user_manager.new_user('invite')
            return 'invite'
        player = input('Which player do you want to play with ? \n')
        player_exists = user_manager.get_user_files().__contains__(player + '.json')
        if player == "":
            print(f"Great ! You play as invite ")
            return "invite"
        else:
            while not player_exists:
                player = input('Player not found, try again \n')
                player_exists = user_manager.get_user_files().__contains__(player + '.json')
                if player == "":
                    print(f"Great ! You play as invite ")
                    return "invite"
    print(f"Great ! You play as {player} ")
    return player


def games_menu():
    """
        Display games menu and user choose between games or return to main_menu
        :return: int
    """
    manage_choice = 0
    while manage_choice != 1 and manage_choice != 2 and manage_choice != 3:
        manage_choice = input('''
            [1] - Mystery number
            [2] - Rock paper scissors
            [3] - return to main menu
            ''')
        if not utils.check_special_characters(manage_choice):
            manage_choice = 0
        manage_choice = int(manage_choice)
    if manage_choice == 1:
        player = choose_player()
        result = mystery_number.mystery_number(player)
        check_win(result)
    if manage_choice == 2:
        player = choose_player()
        result = rock_paper_scissors.mystery_number(player)
        check_win(result)
    if manage_choice == 3:
        return "main"
    return manage_choice


def check_win(game_result: []):
    """
        Check and return true if user wins
        increment nb fail or nbwin user's property if fails or wins
        :param: array
        :return: boolean
    """
    user_manager.add_played_game(game_result[2])
    if game_result[0] == 1:
        if game_result[3] == "shifoumi":
            print(f"You won with {game_result[1]} attempts")
        else:
            print(f"You won with {game_result[1]} points")
        user_manager.add_win(game_result[2])
        return True
    elif game_result[0] == -1:
        print('You loose because you doesn\'t find the number before the last attempt')
        user_manager.add_fail(game_result[2])
        return False
    elif game_result[0] == -2:
        print('You loose because you are a monkey')
        user_manager.add_fail(game_result[2])
        return False


def main():
    user_choice = 0
    while user_choice != 1 and user_choice != 2 and user_choice != 3:
        user_choice = input(
            """
            [1] - Start the game   
            [2] - Manage users
            [3] - Exit the game
            """)
        if not utils.check_special_characters(user_choice):
            user_choice = 0
        else:
            user_choice = int(user_choice)
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
