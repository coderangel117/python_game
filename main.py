import curses
import json

from pick import pick

import mystery_number
import rock_paper_scissors
import tic_tac_toe
import user_manager
import utils
import snake


def choose_player(stdscr):
    """
    user can choose with wich profile he wants to play
    :return: str
    """
    users = user_manager.get_user_files()
    user_manager.merge_json_files(users)
    with open("users.json") as users:
        tab = json.load(users)
        if tab:
            title = "Which player do you want to play with ? \n"
            options = []
            for i in range(len(tab)):
                options.append(tab[i]["username"])
            player, index = pick(options, title, screen=stdscr)
            stdscr.addstr(9, 0, f"You play as {player} \n")
            return player
        else:
            print("No user found in list... \nUser invite (default) selected ")
            user_manager.new_user("invite", stdscr)
            return "invite"  # if no user exists a default user is created and selected to play


def games_menu(stdscr):
    """
    Display games menu and user choose between games or return to main_menu
    :return: int
    """
    title = """ Choose your game """
    options = [
        "Mystery number",
        "Rock paper scissors",
        "Tic Tac Toe",
        "Snake",
        "Return to main menu",
    ]
    _, manage_choice = pick(options, title, screen=stdscr)
    if manage_choice == 0:
        player = choose_player(stdscr)
        result = mystery_number.mystery_number(player, stdscr)
        check_win(result, stdscr)
    if manage_choice == 1:
        player = choose_player(stdscr)
        result = rock_paper_scissors.rock_paper_scissors(player, stdscr)
        check_win(result, stdscr)
    if manage_choice == 2:
        player = choose_player(stdscr)
        result = tic_tac_toe.tic_tac_toe(player, stdscr)
        check_win(result, stdscr)
    if manage_choice == 3:
        player = choose_player(stdscr)
        result = snake.snake(player, stdscr)
        check_win(result, stdscr)
    if manage_choice == 4:
        return "main"
    return manage_choice


def check_win(game_result: [], stdscr):
    """
    Check and return true if user wins
    increment nb fail or nbwin user's property if fails or wins
    :param: array
    :return: boolean
    """
    user_manager.add_played_game(game_result[2])
    if game_result[0] == 1:
        if game_result[3] == "mystery_number":
            stdscr.addstr(3,0,f"You won with {game_result[1]} attempts")
        elif game_result[3] == "shifoumi":
            stdscr.addstr(3,0,f"You won with {game_result[1]} points")
        elif game_result[3] == "snake":
            stdscr.addstr(3,0,f"You ate {game_result[1]} apples")
        user_manager.add_win(game_result[2])
        return True

    elif game_result[0] == -1:
        stdscr.addstr(4, 0, """You loose because you doesn't
            find the number before the last attempt""")
        stdscr.getch()
        user_manager.add_fail(game_result[2])
        return False
    elif game_result[0] == -2:
        stdscr.addstr(4, 0, "You loose because you are a monkey")
        stdscr.getch()
        user_manager.add_fail(game_result[2])
        return False


def main(stdscr):
    if not user_manager.find_user("invite"):
        utils.init_json_files()
    running = True
    while running:
        title = "Welcome to the game center"
        options = ["Start", "Users menu", "Quit"]
        _, user_choice = pick(options, title, screen=stdscr)
        if user_choice == 0:
            result = games_menu(stdscr)
            while result != "main":
                result = games_menu(stdscr)
        elif user_choice == 1:
            choice = user_manager.users_menu(stdscr)
            while choice != "main":
                choice = user_manager.users_menu(stdscr)
        else:
            running = False
            stdscr.addstr("Bye\n")
            stdscr.refresh()
            return 1


if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        utils.handle_exit()
