import curses
import random

from utils import check_special_characters


# @TODO: Add different difficulty ( number of attempts or greater score as possible)
def mystery_number(player: str, stdscr) -> []:
    """
    This function is the implementation of the mystery number game
    :param player:
    :param stdscr:
    :return: return_table:array with the result of the game
    """
    return_table = []
    win = 0  # When user finds the great number
    counter = 0  # The user's attempt count
    max_counter = 10
    force_counter = 0  # Increment when user doesn't respect game's instructions
    fail_counter = False  # Become True when user has exceeded max attempts
    user_number = 0
    number_min: int = 1
    number_max: int = 100
    random_number = random.randint(number_min, number_max)
    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(
        0,
        0,
        f"Hello {player}, try to find the mystery number between {number_min} and {number_max}  ({random_number} attempts) )",
    )
    stdscr.addstr(1, 0, "Press any key to start the game")
    stdscr.getch()
    stdscr.clear()
    while win == 0 & fail_counter is not True:
        while (
            user_number
            != random_number | fail_counter
            is not True | win
            != -1 | win
            != -2
        ):
            stdscr.clear()
            stdscr.addstr(1, 0, "Type a number between 1 and 100\n")
            curses.echo()
            stdscr.refresh()
            try:
                user_number = stdscr.getstr(2, 0).decode("utf-8")
            except curses.error:
                break
            curses.noecho()
            if not check_special_characters(user_number):
                force_counter += 1
                stdscr.addstr(3, 0, "Press a key to continue")
                stdscr.refresh()
                stdscr.getch()
                stdscr.clear()
                break
            user_number = int(user_number)
            if user_number == 0 or user_number > number_max or user_number < number_min:
                if force_counter >= 5:
                    win = -2
                    break
                else:
                    stdscr.addstr(
                        3, 0, f"It's between {number_min} and {number_max} ...."
                    )
                    force_counter += 1
                    break
            if user_number == random_number:
                counter += 1
                win = 1
                break
            if user_number > random_number:
                stdscr.addstr(3, 0, "Your number is bigger than the mystery number")
                if counter < (max_counter - 1):
                    stdscr.addstr(
                        4, 0, f" You have  {(max_counter - 1) - counter} attempts"
                    )
            if user_number < random_number:
                stdscr.addstr(3, 0, "Your number is smaller than the mystery number")
                if counter < (max_counter - 1):
                    stdscr.addstr(
                        4, 0, f"You have {(max_counter - 1) - counter} attempts yet"
                    )
            counter += 1
            if counter == max_counter:
                fail_counter = True
                stdscr.addstr(5, 0, "You have exceeded the maximum number of attempts")
                stdscr.addstr(6, 0, f"the mystery number was {random_number}")
                stdscr.getch()
                win = -1
    return_table.append(win)
    return_table.append(counter)
    return_table.append(player)
    return_table.append("mystery_number")
    return return_table
